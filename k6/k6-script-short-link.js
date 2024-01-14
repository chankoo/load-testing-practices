import http from 'k6/http';
import { sleep, check, fail } from 'k6';

export let options = {
  vus: 1000,
  duration: "5s",
  discardResponseBodies: true,
};
var baseUrl = 'http://alb-short-link-1813400222.ap-northeast-2.elb.amazonaws.com';
// baseUrl = 'http://0.0.0.0';
const testRead = async () => {
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
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
    "url": "https://concurrency-1000-redis-lock.com",
  }
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