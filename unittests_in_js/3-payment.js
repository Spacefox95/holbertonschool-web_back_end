import { Utils } from "./utils.js";

export function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const result = Utils.calculateNumber("SUM", totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
}
