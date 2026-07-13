pragma solidity ^0.8.0;
contract Gov {
    mapping(address => uint) public votes;
    bool public passed;
    function vote() public { votes[msg.sender] += 1; }
    function execute() public { if (votes[msg.sender] >= 1) passed = true; } // VULN: threshold=1
}