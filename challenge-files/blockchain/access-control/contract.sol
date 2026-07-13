pragma solidity ^0.8.0;
contract Vault {
    address public owner;
    mapping(address => uint) public balances;
    constructor() { owner = msg.sender; }
    // VULN: withdraw has no access control
    function withdraw(address to) public {
        payable(to).transfer(balances[to]);
        balances[to] = 0;
    }
}