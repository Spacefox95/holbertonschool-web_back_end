import { createQueue } from "kue";

const queue = createQueue();

const data = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

const job = queue
  .create("push_notification_code", data)
  .save((err) => {
    if (!err) {
      console.log("Notification job created:", job.id);
    } else {
      console.log("Notification job failed");
    }
  })
	.on('complete', () => {
		console.log('Notification job completed')
	})

	.on('failed', () => {
		console.log('Notification job failed')
	})
