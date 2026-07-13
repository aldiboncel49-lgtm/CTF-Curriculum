pragma solidity ^0.8.0;
interface IERC20 { function balanceOf(address) external view returns (uint); }
contract AMM {
    uint public price;
    function flashLoan(address token, address attacker) public {
        uint b = IERC20(token).balanceOf(address(this));
        price = 999; // VULN: price manipulated during callback
        require(IERC20(token).balanceOf(address(this)) == b, "repaid");
    }
}