pragma solidity ^0.8.0;
contract Inbox {
    address public sequencer;
    mapping(address => uint) public credits;
    function forceInclude(address user) public {
        // VULN: anyone can force-include, bypassing sequencer ordering
        credits[user] += 1;
    }
}