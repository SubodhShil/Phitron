let previousDepositValue = 0;
let totalDepositAmount = parseFloat(
    document.getElementById("deposit-value").innerText
);

let previousWithdrawValue = 0;
let totalWithdrawAmount = 0;

document.getElementById("total").innerText = totalDepositAmount;
let totalAmount = 0;

function handleDeposite(e) {
    previousDepositValue = parseFloat(
        document.getElementById("deposit-value").innerText
    );
    totalDepositAmount = 0;

    let depositeInput = document.getElementById("deposit-input");

    // Error handling
    let depositAmount = 0;

    if (depositeInput.value > 0) {
        depositAmount = parseFloat(depositeInput.value);
    }

    totalDepositAmount = previousDepositValue + depositAmount;

    // update total
    totalAmount = totalDepositAmount;
    // update value in total div
    document.getElementById("total").innerText = totalAmount;

    console.log(`Deposit value (total) is: ${totalDepositAmount}`);

    // ^ update in the UI
    document.getElementById("deposit-value").innerText = totalDepositAmount;
}

function handleWithdraw(e) {
    previousWithdrawValue = parseFloat(
        document.getElementById("withdraw-value").innerText
    );
    let withdrawInput = document.getElementById("withdraw-input");

    // Error handling
    let withdrawAmount = 0;

    if (withdrawInput.value > 0) {
        withdrawAmount = parseFloat(withdrawInput.value);
    }

    totalWithdrawAmount = previousWithdrawValue + withdrawAmount;

    // Error handling 2
    if (totalWithdrawAmount < totalDepositAmount) {
        totalDepositAmount -= totalWithdrawAmount;
        // update total
        totalAmount = totalDepositAmount;
    }

    // update value in total div
    document.getElementById("total").innerText = totalAmount;

    console.log(`Withdraw value is: ${totalWithdrawAmount}`);

    // ^ update in the UI
    document.getElementById("withdraw-value").innerText = totalWithdrawAmount;
}
