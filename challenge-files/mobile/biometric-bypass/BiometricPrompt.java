// VULN: onAuthenticationFailed still grants access
public void onAuthenticationError(...) { grantAccess(); }