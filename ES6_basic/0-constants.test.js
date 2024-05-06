// tasks.test.js
import { taskFirst, getLast, taskNext } from './0-constants';

describe('taskFirst', () => {
  test('should return a string containing "I prefer const when I can."', () => {
    expect(taskFirst()).toBe('I prefer const when I can.');
  });
});

describe('getLast', () => {
  test('should return a string containing " is okay"', () => {
    expect(getLast()).toBe(' is okay');
  });
});

describe('taskNext', () => {
  test('should return a string combining "But sometimes let" and the result of getLast()', () => {
    const expectedResult = 'But sometimes let is okay';
    expect(taskNext()).toBe(expectedResult);
  });
});
