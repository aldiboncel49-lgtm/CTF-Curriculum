pragma solidity ^0.8.0;
contract Token {
    mapping(address => uint256) public balance;
    function transfer(address to, uint256 amt) public {
        unchecked { balance[msg.sender] -= amt; } // VULN: underflow
        balance[to] += amt;
    }
}