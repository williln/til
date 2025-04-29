# Bot Fight Mode

If your site is getting hammered by bots and triggering a ton of errors, and you use Cloudflare, one of your options is to use [Bot Fight Mode](https://developers.cloudflare.com/learning-paths/get-started-free/security/bot-fight-mode/?utm_source=chatgpt.com).

This will put that "are you a human?" check in front of your sites.

A note: In the "free" tier of Bot Fight Mode, you can't customize it at all. This may have side effects, like your site blocking webhooks you subscribe to from external sites (like Stripe).

The docs on Bot Fight Mode are pretty light; it's basically an on/off switch.

There is also [Super Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/), which costs money (it's part of one of their subscription tiers), which is customizable to a degree. At this level, it seems like you can [set rules](https://developers.cloudflare.com/bots/get-started/super-bot-fight-mode/#conditions) to "Skip action" and specify parts of your site where the Super Bot Fight Mode should not run (like, potentially, your webhook endpoints?)

In my experience, turning on Bot Fight Mode does seem to block legitimate webhook traffic. I haven't tried Super Bot Fight Mode, so I'm not sure about the specifics of the rule-setting capabilities.

There is also [Bot Management for Enterprise](https://developers.cloudflare.com/bots/get-started/bot-management/), but I'm not sure what that gets you beyond Super Bot Fight Mode.
