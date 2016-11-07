Sprint Topics
#############

:slug: topics
:summary: topics


Pyramid 2.0
===========

There has been a lengthy discussion about what should go into Pyramid 2.0. The entire story is on https://github.com/Pylons/pyramid/issues/2362, let's just have a quick summary here:

Likely
------

* Remove check_csrf view predicate in favor of require_csrf (already deprecated).
* Remove custom_predicates from config.add_view and view_config (already deprecated).
* Remove config.set_request_property (already deprecated).

Interesting, let's open an issue and talk about it
--------------------------------------------------

* Something to do with route prefixes so that it's possible to use config.include without the base url inside having a / suffix. #406, #1639
* Drop PasteDeploy in favor of a better loading system. #2419
* Fix predicate factories to accept a standardized info object instead of config. Currently the only purpose of this argument is for config.maybe_dotted but it's poor practice to pass the ephemeral config object around. #2535

Interesting but unlikely without a champion to start the discussion
-------------------------------------------------------------------

* Deprecate remember/forget APIs in favor of a pattern that fits better with non-cookie workflows.
* Something to do with identity and auth-api post mortem?
* Remove pcreate and default scaffolds. #2384
* Add a public API at the top-level pyramid namespace. For example pyramid.view_config, pyramid.Configurator, etc. This would greatly assist in maintainability of the public API for people using IDEs like pycharm where they may not be checking the docs to ensure an API is public. Probably use a lazy-instantiator like apipkg for this. #2387
* Switch the ISession contract from pickleable objects to something more secure and portable like json. #2709
* Separate CSRF tokens from the ISession into something else implementable without a session.
* Re-work view_config to namespace arguments to be more clear about options versus predicates.
* Re-work config.add_view, config.add_forbidden_view, config.add_notfound_view to accept only kwargs. Almost all of the parameters are indistinguishable from user-defined view options, so they could be treated all the same.
* Separate NotFound and Forbidden exceptions from HTTPNotFound and HTTPForbidden. This would undo previous work to merge them in order to make exception views more understandable.

DragonSprint is a perfect opportunity to discuss these issues and decide what the next steps are.


Pyramid for Newcomers
=====================

Those of us that use Pyramid know how great it is. But unfortunately, when I go to Python conferences around Europe, not many people know Pyramid. Why is that?

We are gonna be holding a thorough research into what we as a community can do to make Pyramid more visible to the Python community and how to make our docs better. Let's find out what other communities such as Flask, Django, even Plone are doing right and see if we can duplicate their results.

Just some random ideas:

* Is there a tutorial topic that is popular between Web frameworks and Pyramid does not have it?
* create Pyramid cheat-sheet for DuckDuckGo
* automatic Tweets for new Pyramid releases
* update http://www.pylonsproject.org/ with up-to-date content and graphics
* make the expirience for new contributors nicer (i.e. what Coala folks are doing)
* create a "Heroku button" so it's super easy to get your own install of Pyramid online in no time
* Pyramid success stories
* Donation page


Want to work on something else?
===============================

By all means do! Since sprints are of open nature, anyone can and should suggest a topic!
