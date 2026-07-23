/* ==========================================================
   MOTORBIKE RENTAL SYSTEM
   CUSTOMER BOOKING TRACKER
========================================================== */

// Current booking status
// This value will later come from Django

//let currentStatus = "Confirmed";
let currentStatus = bookingStatus;

// All booking stages

const stages = [
  {
    name: "Request Booking",
    icon: "📝",
  },

  {
    name: "Pending",
    icon: "⏳",
  },

  {
    name: "Approved",
    icon: "✔",
  },

  {
    name: "Confirmed",
    icon: "💳",
  },

  {
    name: "Ready for Collection",
    icon: "🛠",
  },

  {
    name: "Active Hire",
    icon: "🏍",
  },

  {
    name: "Completed",
    icon: "🏁",
  },
];

// Find current stage position

function getCurrentStage() {
  return stages.findIndex((stage) => stage.name === currentStatus);
}

// Create tracker

function createTracker() {
  const tracker = document.getElementById("progressTracker");

  if (!tracker) return;

  const current = getCurrentStage();

  tracker.innerHTML = "";

  stages.forEach((stage, index) => {
    let status = "waiting";

    if (index < current) {
      status = "completed";
    } else if (index === current) {
      status = "active";
    }

    tracker.innerHTML += `


            <div class="timeline-item ${status}">


                <div class="circle">

                    ${stage.icon}

                </div>


                <div class="stage-name">

                    ${stage.name}

                </div>


            </div>



            ${
              index !== stages.length - 1
                ? `<div class="connector ${
                    index < current ? "completed-line" : ""
                  }"></div>`
                : ""
            }


            `;
  });
}

// Start tracker

document.addEventListener("DOMContentLoaded", () => {
  createTracker();

  startCountdown();
});

/* ==========================================================
   COLLECTION COUNTDOWN
========================================================== */

function startCountdown() {
  const targetDate = new Date("July 20, 2026 09:00:00").getTime();

  const timer = document.getElementById("countdown");

  if (!timer) return;

  setInterval(() => {
    const now = new Date().getTime();

    const distance = targetDate - now;

    if (distance < 0) {
      timer.innerHTML = "Collection Time";

      return;
    }

    const days = Math.floor(distance / (1000 * 60 * 60 * 24));

    const hours = Math.floor(
      (distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60),
    );

    const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));

    timer.innerHTML = `
        ${days} Days
        <br>
        ${hours} Hours
        <br>
        ${minutes} Minutes

        `;
  }, 1000);
}
