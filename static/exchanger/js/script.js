const dropList = document.querySelectorAll("form select"),
fromCurrency = document.querySelector(".from select"),
toCurrency = document.querySelector(".to select"),
getButton = document.querySelector("form button");

// Kriptovalyutalar va O'zbekiston so'mi ro'yxati
const currencies = [
    {code: "BTC", name: "Bitcoin"},
    {code: "ETH", name: "Ethereum"},
    {code: "USDT", name: "Tether"},
    {code: "BNB", name: "Binance Coin"},
    {code: "UZS", name: "O'zbekiston so'mi"}
];

// Tanlash elementlariga valyutalarni qo'shish
currencies.forEach(currency => {
    let option = `<option value="${currency.code}">${currency.name}</option>`;
    fromCurrency.insertAdjacentHTML("beforeend", option);
    if (currency.code !== "UZS") {
        toCurrency.insertAdjacentHTML("beforeend", option);
    }
});

// Standart holatda BTC va UZS tanlangan
fromCurrency.value = "BTC";
toCurrency.value = "UZS";

// Valyuta kursi olish va konvertatsiya qilish funksiyasi
async function getExchangeRate() {
    const amount = document.querySelector("form input");
    const exchangeRateTxt = document.querySelector("form .exchange-rate");
    let amountVal = amount.value;
    if(amountVal == "" || amountVal == "0"){
        amount.value = "1";
        amountVal = 1;
    }
    exchangeRateTxt.innerText = "Kurs olinmoqda...";

    try {
        // Bu yerda haqiqiy API so'rovini amalga oshirishingiz kerak
        // Misol uchun:
        // const response = await fetch(`https://api.example.com/v1/exchangerate/${fromCurrency.value}/${toCurrency.value}`);
        // const result = await response.json();
        // let exchangeRate = result.rate;

        // Hozircha shartli qiymat
        let exchangeRate = 100000000; // 1 BTC = 100,000,000 UZS

        let totalExRate = (amountVal * exchangeRate).toFixed(2);
        exchangeRateTxt.innerText = `${amountVal} ${fromCurrency.value} = ${totalExRate} ${toCurrency.value}`;
    } catch(error) {
        exchangeRateTxt.innerText = "Xatolik yuz berdi";
    }
}

getButton.addEventListener("click", (e) => {
    e.preventDefault();
    getExchangeRate();
});

window.addEventListener("load", getExchangeRate);