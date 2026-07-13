pragma solidity ^0.8.0;
contract Bank {
    mapping(address => uint) public bal;
    function deposit() public payable { bal[msg.sender] += msg.value; }
    function withdraw(uint amt) public {
        require(bal[msg.sender] >= amt);
        (bool ok,) = msg.sender.call{value: amt}(""); // VULN: external call before update
        bal[msg.sender] -= amt;
    }
}