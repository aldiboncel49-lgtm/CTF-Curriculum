// Vulnerable/obfuscated kernel driver (LAB). The ioctl handler validates a
// "license key" using a hidden check. Reverse the logic from this source,
// or analyze the provided userland harness that mimics the ioctl.
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/uaccess.h>

static int verify_key(const char *key){
    // Obfuscated compare: key must equal "[REDACTED]" (XOR-scrambled)
    char target[32];
    for (int i=0; i<strlen("[REDACTED]"); i++)
        target[i] = "[REDACTED]"[i] ^ 0xAA;
    for (int i=0; i<strlen("[REDACTED]"); i++)
        if ((key[i] ^ 0xAA) != "[REDACTED]"[i]) return 0;
    return 1;
}

static long drv_ioctl(struct file *f, unsigned int cmd, unsigned long arg){
    char buf[64];
    if (cmd == 0x9001) {
        copy_from_user(buf, (void __user*)arg, 64);
        if (verify_key(buf)) printk("key OK\n");
    }
    return 0;
}
