import { expect } from 'chai';
import sinon from 'sinon';
import { Utils } from './utils.js';
import { sendPaymentRequestToApi } from './4-payment.js';

describe("sendPaymentRequestToApi", function () {
  let stub;
  let consoleSpy;

  beforeEach(() => {
    stub = sinon.stub(Utils, "calculateNumber").returns(10);
    consoleSpy = sinon.spy(console, "log");
  });

  afterEach(() => {
    stub.restore();
    consoleSpy.restore();
  });

  it("should stub Utils.calculateNumber and log the correct message", () => {
    sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnce).to.be.true;
    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(consoleSpy.calledOnceWithExactly("The total is: 10")).to.be.true;
  });
});
