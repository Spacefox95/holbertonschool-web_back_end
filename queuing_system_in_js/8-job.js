function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }

  for (const jobData of jobs) {
    const job = queue.create("push_notification_code_3", jobData);
    job
      .save((err) => {
        if (!err) {
          console.log("Notification job created:", job.id);
        }
      })
      .on("complete", () => {
        console.log(`Notification job ${job.id} completed`);
      })

      .on("progress", (percentage) => {
        console.log(`Notification job ${job.id} ${percentage}% complete`);
      })

      .on("failed", (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
  }
}

export default createPushNotificationsJobs;