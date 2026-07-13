pragma solidity ^0.8.0;
contract Swap {
    uint public reserve0; uint public reserve1;
    function swap(uint in0) public returns (uint out1) {
        out1 = reserve1 * in0 / (reserve0 + in0); // VULN: no slippage guard
        reserve0 += in0; reserve1 -= out1;
    }
}