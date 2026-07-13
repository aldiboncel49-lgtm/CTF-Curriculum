// Vulnerable kernel module (LAB: load on a test VM, then exploit from userland)
// Provides a /proc/kerntest ioctl that performs an unchecked copy_from_user,
// enabling a ret2usr / kernel ROP chain to escalate privileges (commit_creds(prepare_kernel_cred(0))).
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/proc_fs.h>
#include <linux/uaccess.h>

#define CMD_RUN 0x1337
static struct proc_dir_entry *ent;

// VULN: buffer is on kernel stack, copy_from_user size unchecked
static long dev_ioctl(struct file *f, unsigned int cmd, unsigned long arg){
    char buf[64];
    if (cmd == CMD_RUN) {
        // MISSING: copy_from_user size bound -> stack overflow in kernel
        copy_from_user(buf, (void __user *)arg, 256);
    }
    return 0;
}

static const struct file_operations fops = { .unlocked_ioctl = dev_ioctl };

static int __init krop_init(void){
    ent = proc_create("kerntest", 0666, NULL, &fops);
    printk("kerntest loaded\n");
    return 0;
}
static void __exit krop_exit(void){ remove_proc_entry("kerntest", NULL); }
module_init(krop_init); module_exit(krop_exit);
MODULE_LICENSE("GPL");
