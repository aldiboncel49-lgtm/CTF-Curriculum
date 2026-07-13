pragma solidity ^0.8.0;
contract Proxy {
    address public impl;
    uint public owner;
    function setImpl(address a) public { impl = a; }
    function exec() public { (bool ok,) = impl.delegatecall(msg.data); } // VULN
}