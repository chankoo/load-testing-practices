import http from 'k6/http';
import { sleep, check, fail } from 'k6';


export let options = {
  vus: 10,
  duration: "3m",
  discardResponseBodies: true,
};


const test = async () => {
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };
  const url1 = 'http://alb-ecs-1586857067.ap-northeast-2.elb.amazonaws.com/v1/me/posts/';
  const payload = JSON.stringify({
    "person": 1,
    "content": '국회에 제출된 법률안 기타의 의안은 회기중에 의결되지 못한 이유로 폐기되지 아니한다. 다만, 국회의원의 임기가 만료된 때에는 그러하지 아니하다. 국회는 법률에 저촉되지 아니하는 범위안에서 의사와 내부규율에 관한 규칙을 제정할 수 있다.\n' +
        '\n' +
        '형사피의자 또는 형사피고인으로서 구금되었던 자가 법률이 정하는 불기소처분을 받거나 무죄판결을 받은 때에는 법률이 정하는 바에 의하여 국가에 정당한 보상을 청구할 수 있다.',
  });
  const res1 = await http.post(url1, payload, params);
  const checkResult1 = check(res1, {
    'is status 200': (r) => r.status === 201,
  });
  if (!checkResult1) {
    fail('Failed due to an unexpected status code: ' + res1.status);
  }
  sleep(1);
}

export default test;