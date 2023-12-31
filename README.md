# IR_REMOTE_RPI0W2

```sh
sudo apt-get install python3-pip git pigpio python3-pigpio
sudo apt-get install i2c-tools libi2c-dev
sudo systemctl enable pigpiod.service
sudo systemctl start pigpiod

pip install flask flask-cors flask-restful smbus
```



* `sudo raspi-config`
* `Interface Options`
 * `I2C Enable`


`/boot/config.txt`

```sh
...
dtparam=i2c_arm=off
...
dtoverlay=gpio-shutdown,gpio_pin=3,active_low=1,debounce=1000
gpio=27=op,dh
dtoverlay=i2c-gpio,bus=11,i2c_gpio_sda=25,i2c_gpio_scl=26
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