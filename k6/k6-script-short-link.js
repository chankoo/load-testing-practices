import http from 'k6/http';
import { sleep, check, fail } from 'k6';

export let options = {
  vus: 1000,
  duration: "20s",
  discardResponseBodies: true,
};

const test = async () => {
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const baseUrl = 'http://0.0.0.0';
  const path = '/short-links'
  const shortId = '100'
  const res1 = await http.get(baseUrl + path + '/' + shortId, params);
  const checkResult1 = check(res1, {
    'success': (r) => r.status == 200,
  });
  if (!checkResult1) {
    fail('Failed due to an unexpected status code: ' + res1.status);
  }
  sleep(1);
}

export default test;