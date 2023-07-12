package Completed

import kotlin.math.*

fun main() {
    val n = readLine()!!.toInt();
    var x = 0.0;
    var y = 0.0;
    for (i in 1..n) {
        var (r, d) = readLine()!!.split(' ').map{it.toInt()};
        d %= 360;
        x += r * sin(d * Math.PI / 180.0);
        y += r * cos(d * Math.PI / 180.0);
    }
    var mag = sqrt(x * x + y * y);
    var deg = atan(abs(y/x)) * 180.0 / Math.PI;
    if (x >= 0 && y < 0) deg = -deg; // quad 4
    else if (x < 0 && y >= 0) deg = 180 - deg; // quad 2
    else if (x < 0 && y < 0) deg = deg + 180; // quad 3
    deg = 90 - deg;
    deg += 360;
    deg %= 360;

    println("${mag.roundToInt()} ${deg.roundToInt()}");
}
