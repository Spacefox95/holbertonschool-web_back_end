import sinon from 'sinon';
import { expect } from 'chai';
import { Utils } from './utils.js';
import { sendPaymentRequestToApi } from './3-payment.js';

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with correct args', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');

    sendPaymentRequestToApi(100, 20);

    expect(spy.calledOnce).to.be.true;
    expect(spy.calledWith('SUM', 100, 20)).to.be.true;

    spy.restore();
  });
});
