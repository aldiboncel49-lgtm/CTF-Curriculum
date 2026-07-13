pragma solidity ^0.8.0;
contract Oracle {
    uint public price;
    function setPrice(uint p) public { price = p; } // VULN: single source, no auth
    function getPrice() public view returns (uint) { return price; }
}