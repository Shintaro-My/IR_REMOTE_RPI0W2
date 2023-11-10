# IR_REMOTE_RPI0W2

```sh
sudo apt-get install python3-pip git pigpio python3-pigpio
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod

```


```js
for(const i of [...Array(12).keys()].map(n => n + 1)) {
    console.log(i);
    var req = await fetch('/api/ir', {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({name: `PANASONIC:TV:CH${('0' + i).slice(-2)}`, desc: `TV Ch${i}`})
    });
    console.log(await req.json());
}
```