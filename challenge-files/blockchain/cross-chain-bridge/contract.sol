pragma solidity ^0.8.0;
contract Bridge {
    mapping(bytes32 => bool) public claimed;
    function claim(bytes32 id) public {
        // VULN: no chainId validation -> replay across chains
        claimed[id] = true;
    }
}