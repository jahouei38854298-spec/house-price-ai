
const form = document.getElementById("prediction-form");

const resultDiv = document.getElementById("result");

const submitButton = form.querySelector("button[type='submit']");


// نمایش پیام در صفحه
function showMessage(message, type) {

    resultDiv.textContent = message;

    resultDiv.className = `result ${type}`;
}


// تبدیل خطاهای اعتبارسنجی FastAPI به فارسی
function translateError(errors) {

    const messages = {
        area: "متراژ خانه باید بین 80 تا 180 باشد.",
        rooms: "تعداد اتاق‌ها باید بین 2 تا 5 باشد.",
        age: "سن خانه باید بین 1 تا 10 سال باشد."
    };

    if (Array.isArray(errors)) {

        const field = errors[0]?.loc?.[1];

        return messages[field] || "اطلاعات واردشده معتبر نیست.";

    }

    return "اطلاعات واردشده معتبر نیست.";
}


// مدیریت ارسال فرم
form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const area = Number(document.getElementById("area").value);

    const rooms = Number(document.getElementById("rooms").value);

    const age = Number(document.getElementById("age").value);


    // غیرفعال کردن دکمه
    submitButton.disabled = true;

    submitButton.textContent = "در حال محاسبه...";


    // نمایش وضعیت انتظار
    showMessage("لطفاً منتظر بمانید...", "loading");


    try {

        const response = await fetch("/predict", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                area: area,
                rooms: rooms,
                age: age
            })

        });


        const data = await response.json();


        // بررسی خطای API
        if (!response.ok) {

            if (response.status === 422) {

                throw new Error(translateError(data.detail));

            }

            throw new Error("خطا در انجام پیش‌بینی قیمت خانه.");

        }


        // نمایش نتیجه موفق
        const price = data.predicted_price.toLocaleString("fa-IR");

        showMessage(
            `قیمت پیش‌بینی‌شده خانه: ${price}`,
            "success"
        );


    } catch (error) {

        showMessage(error.message, "error");

    } finally {

        // فعال کردن مجدد دکمه
        submitButton.disabled = false;

        submitButton.textContent = "محاسبه قیمت خانه";

    }

});

// دریافت دکمه پاک کردن فرم
const resetButton = document.getElementById("reset-button");


// مدیریت کلیک روی دکمه پاک کردن
resetButton.addEventListener("click", function() {

    // پاک کردن تمام ورودی‌های فرم
    form.reset();

    // پاک کردن پیام نتیجه
    resultDiv.textContent = "";

    // حذف کلاس‌های وضعیت نتیجه
    resultDiv.className = "result";

});