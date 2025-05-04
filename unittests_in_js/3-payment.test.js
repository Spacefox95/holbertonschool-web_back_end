const sinon = require("sinon");
const { expect } = require("chai");

const sendPaymentRequestToApi = require("./3-payment");
const utils = require("./utils");

describe("sendPaymentRequestToApi", function () {
  const spy = sinon.spy(utils, "calculateNumber");
  const consolespy = sinon.spy(console, "log");

  it("should call Utils.calculateNumber with correct args", () => {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith("SUM", 100, 20)).to.be.true;

    spy.restore();
    consolespy.restore();
  });
});
