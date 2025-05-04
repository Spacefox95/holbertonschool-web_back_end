import { expect } from 'chai';
import sinon from 'sinon';
import './utils';
import { sendPaymentRequestToApi } from './3-payment';

describe("sendPaymentRequestToApi", function () {
  const spy = sinon.spy(Utils, "calculateNumber");

  it("should call Utils.calculateNumber with correct args", () => {
    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith("SUM", 100, 20)).to.be.true;

    spy.restore();
  });
});
