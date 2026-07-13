pragma solidity ^0.8.0;
contract Sender {
    function sendTo(address to, uint amt) public {
        to.call{value: amt}(""); // VULN: return value not checked
    }
}