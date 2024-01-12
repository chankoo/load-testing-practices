import http from 'k6/http';
import { sleep, check, fail } from 'k6';

export let options = {
  vus: 100,
  duration: "5s",
  discardResponseBodies: true,
};

const testRead = async () => {
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

const testCreate = async () => {
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const body = {
    "url": "https://concurrency-100.com",
  }
  const baseUrl = 'http://0.0.0.0';
  const path = '/short-links'
  const res = await http.post(baseUrl + path, JSON.stringify(body), params);
  const checkResult = check(res, {
    'success': (r) => r.status == 200 || r.status == 201,
  });
  if (!checkResult) {
    fail('Failed due to an unexpected status code: ' + res.status);
  }
  sleep(1);
}

export default testCreate;