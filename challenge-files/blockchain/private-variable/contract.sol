pragma solidity ^0.8.0;
contract Secret {
    uint256 private secret;
    string private note;
    constructor() { secret = 0x1337; note = "hidden"; }
    function getNote() public view returns (string memory) { return note; }
    // VULN: secret is readable from storage slot 0
}