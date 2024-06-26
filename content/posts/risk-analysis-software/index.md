+++
linkTitle = "Risk Analysis for Software Projects"
shortTitle = "Risk Analysis Software"
title = "Risk Analysis for Software Projects"
draft = false
genres = ["technical"]
date = 2022-10-11
+++


Revised: August 2023

## Introduction

In regulated engineering, FMEAs, FTAs, and PRAs are common acronyms for risk management documents. Outside of that world, "risk management" is a bit of a snoozer of a topic. Behind this deceptive veneer lie some valuable tools that could benefit software projects at large, and not just in regulated environments.

One of these tools is the FMEA, or **Failure Modes and Effects Analysis**. Before diving into the FMEA though, let's set up a little background information.

!["The Fatigues", Seinfeld (1996)](Seinfeld-RM.png)
_The Fatigues_, Seinfeld (1996)

## Background

In the broader discipline of engineering, a failure can be defined as an unintended consequence in a manufactured item. The manifestation of a failure in software development is commonly known as a bug.

Here is a formalized definition of a bug:  

**Unexpected behavior in a deployed application as a result of code that does not adequately cover all possible field use conditions**

In simpler terms:  

**Code that doesn't behave the way it was designed**

Some bugs are immediately obvious and can be fixed in the moment. Others only manifest themselves in the field or in a production environment. The cost of fixing a bug grows [exponentially](https://deepsource.io/blog/exponential-cost-of-fixing-bugs/) from the time it is created all the way to field deployment. This means the cost to fix a bug in code as soon as one writes the code is very minimal. This is compared to noticing it when the code base is more mature, core engineers have left the project, and eventually the product is deployed to the field and might require a recall. Depending on the software, one might be able to deploy an over-the-air patch, but in critical embedded systems this may not be an option.

!["Russfest", Silicon Valley (2019)](SiliconValley-bugs.jpg)
_Russfest_, Silicon Valley (2019)

### "Just eliminate risk!"

This is extremely concerning to most managers. These situations may be handled with the following phrases:

- _By attaining 100% test coverage, we will eliminate risk from this project._

- _When we can guarantee 99.9999% uptime, we can safely assume that failure will never happen._

- And a personal favorite: _Just eliminate risk!_

!["A.A.R.M.", The Office (2013)](Office-Nonsense.png)
*"A.A.R.M.", The Office (2013)*

With a bold statement like that, context matters. The gold standard in highly regulated industries is 6 nines - or 99.9999% reliability. This corresponds to approximate [3.4 defects per million opportunities of failure](https://en.wikipedia.org/wiki/Six_Sigma#Sigma_levels).

**It is a logical fallacy to state that risk can be eliminated.** Unless one works in first principles where **MAYBE** certain behaviors can be guaranteed, one cannot and should not guarantee that the product, whether that be software or hardware, will never fail. The likelihood of failure might range from common to astronomically rare, but it always exists. For this article, the definition of failure has been left rather broad. In a future article, we'll explore failures with a range of effects, from minimal to catastrophic.

**The goal of risk management is to minimize, not eliminate, risk in a technical project by minimizing the probability of failure and minimizing the impact of failure.**

### How?

How can risk be minimized effectively? There have been books written about the subject, software tools developed, and an entire risk management consulting industry dedicated to aerospace, medical device, and pharmaceutical risk management. One of the core tools used by every company in these industries is called the FMEA.

## The FMEA

The Failure Modes and Effects Analysis, or FMEA, explains how failures at a component level propagate to system failures. This document can get massively complex for large system with many subsystems and components, such as an airplane.

So what's the motivation? Why go to all this effort to analyze a manufactured product from a risk perspective? A good FMEA tells a good story, and it does so in two key ways:

- The FMEA tells a top-down story to regulatory bodies
- The FMEA allows engineers to tell a bottom-up story

When a regulated device fails, the manufacturer has to explain to the regulatory body WHY it failed, and how they will fix it in the future. This is the top-down story. The FDA and FAA are examples of regulated bodies. All they know is that the device failed at the user level, and it's up to the manufacturer to guide them into the details of the device, identify the root cause of the failure, and fix it.

![Component System Failures](Component-System-Failures.png)
*Component System Failures*

If a manufacturer is unable to provide a resolution, the device can be pulled from the market, either voluntarily by the manufacturer or as mandated by a regulatory body. A recent high-profile instance of this was the Boeing 737 MAX, which experienced a software failure in a program called MCAS (Maneuvering Characteristics Augmentation System) and ultimately caused 2 [fatal accidents](https://en.wikipedia.org/wiki/Maneuvering_Characteristics_Augmentation_System).

## An Example

### Setup

Airplanes and medical devices are very complicated systems, so let's use an example everyone is familiar with - a bicycle. Let's pretend that we want to get into the road bike space. Our task as engineers is to build a bicycle that is fast and safe. After all, if we want to sell our bike, we need to both convince customers that it's fast enough to win races, and safe enough to meet the minimum requirements imposed by the FBA (Federal Bicycle Administration), an imaginary entity that allows manufacturers to sell bicycles in the United States.

![Bicycle Components](Bicycle-Components.png)
*Bicycle Components*

### Components and Functions

The first step is to define the system architecture. Let's call this grouping of top-level entities **Components**. On our bicycle I’ll keep things simple and only analyze the _Drivetrain_, _Brakes_, and _Frame_ for this example. Of course there are many other subsystems we could define and analyze as well, and we could even slice-and-dice the bike architecture in a different way depending on the goals of our analysis.

Some important questions to answer include:

- _What is the boundary of analysis for each component?_ This means, what sub-components of the bicycle are members of the drivetrain, which are components of the brake, and which are components of the frame?
- _What are the functions of each component?_ What are some primary and secondary purposes of the drivetrain, the brakes, and the frame?

Let's build an actual FMEA for our bicycle. The primary function of the drivetrain is to move the bicycle forwards. In engineering terms we can state this as _Converting rotational motion into horizontal motion_. The primary function of the brakes is to bring the bicycle to a stop, which we can state as _Converting kinetic energy into heat_. Finally, the frame has two functions: _Supporting the cyclist_ and _Supporting the components of the bicycle_.

---

<span style = 'color: green; font-size: 32px;'>**Component:** Drivetrain</span><br>
<span style = 'color: green;'>**Function:** Convert rotational motion into horizontal motion</span><br>

<span style = 'color: red; font-size: 32px;'>**Component:** Brakes</span><br>
<span style = 'color: red'>**Function:** Convert kinetic energy into heat</span><br>

<span style = 'color: blue; font-size: 32px;'>**Component:** Frame</span><br>
<span style = 'color: blue'>**Function:** Support the cyclist</span><br>
<span style = 'color: blue'>**Function:** Support the components of the bicycle</span><br>

---

### Failure Modes

Ok great! So now that we have defined some components and each of their functions, let’s take a look at how these components can fail. (As a little sneak peak, we will be able to recursively define each subsequent level of analysis. In a later example, we will consider the Drivetrain as its own system, identify its Components, and so on.)

A convenient and standard way to define how a component might fail is by writing the Failure Mode as an anti-function. Generally, this would be written something like:

The _Component_ fails to _deliver the function_.

For our drivetrain, we would say that _the Drivetrain fails to convert rotational motion into horizontal motion_. This might seem pretty obvious and redundant, but simple verbiage like this keeps things consistent across our risk analysis. This allows us to focus on why things are failing, and how to mitigate those failures.

Let’s use this same template to come up with failure modes for the Brakes and Frame. A way that our brakes can fail is by _failing to convert kinetic energy into heat_. Since our frame has two functions, we can write two failure modes, one for each function - _Frame fails to support cyclist_, and _Frame fails to support components_.

---

<span style = 'color: green; font-size: 32px;'>**Component:** Drivetrain</span><br>
<span>**Function:** Convert rotational motion into horizontal motion</span><br>
<span style = 'color: green; margin-left: 40px;'>**Failure Mode:** Drivertrain fails to convert rotational motion into horizontal motion</span><br>

<span style = 'color: red; font-size: 32px;'>**Component:** Brakes</span><br>
<span>**Function:** Convert kinetic energy into heat</span><br>
<span style = 'color: red; margin-left: 40px;'>**Failure Mode:** Brakes fail to convert kinetic energy into heat</span><br>

<span style = 'color: blue; font-size: 32px;'>**Component:** Frame</span><br>
<span>**Function:** Support the cyclist</span><br>
<span style = 'color: blue; margin-left: 40px;'>**Failure Mode:** Frame fails to support cyclist</span><br>
<span>**Function:** Support the components of the bicycle</span><br>
<span style = 'color: blue; margin-left: 40px;'>**Failure Mode:** Frame fails to support components</span><br>

---

Great! We’ve come up with a bunch of ways that our bike can fail. But are these the only ways these components can fail? Of course not! There are a wide variety of ways anything can fail, and not just catastrophically as we seem to have defined here.

As a reminder, a failure mode is defined as _the manner in which a component fails to meet or deliver its intended function_. According to risk management theory, there are [6 main ways](https://www.elsevier.com/books/safety-risk-management-for-medical-devices/elahi/978-0-323-85755-0) most components can fail. The component:

- Has no ability to perform the function
- Delivers only part of the function
- Delivers excessive function
- Delivers intermittent function
- Delivers a degraded function
- Delivers function at the wrong time

Armed with this new information, let’s head back to our risk analysis. I think total brake failure is an important consideration, but not the only way our bicycle can fail to stop. Partial brake failure is pretty common and can be just as dangerous, so let’s incorporate that into our analysis.

---

<span style = 'color: green; font-size: 32px;'>**Component:** Drivetrain</span><br>
<span>**Function:** Convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Drivertrain fails to convert rotational motion into horizontal motion</span><br>

<span style = 'color: red; font-size: 32px;'>**Component:** Brakes</span><br>
<span>**Function:** Convert kinetic energy into heat</span><br>
<span style = 'color: red; margin-left: 40px;'>**Failure Mode:** Brakes COMPLETELY fail to convert kinetic energy into heat</span><br>
<span style = 'color: red; margin-left: 40px;'>**Failure Mode:** Brakes PARTIALLY fail to convert kinetic energy into heat</span><br>

<span style = 'color: blue; font-size: 32px;'>**Component:** Frame</span><br>
<span>**Function:** Support the cyclist</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support cyclist</span><br>
<span>**Function:** Support the components of the bicycle</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support components</span><br>

---

I’ve updated our existing failure mode to reflect total brake failure, and I’ve created a new one called _Brakes PARTIALLY fail to convert kinetic energy into heat._ We’ll find that when it comes time to mitigate these risks, we can address each individually with some specific mitigation plans.

---

Whew! We’ve gone through a lot so far, so let’s take a breather and let some of this sink in.

The reason we’re doing this analysis is to understand the risk profile of a bicycle more thoroughly. We are pretending that we are the manufacturer of the bicycle, and we need to first and foremost demonstrate that our bicycle is safe to operate in its intended use conditions. As competent mechanical engineers in the field of bicycle manufacturing, we will always strive to design a safe bicycle. As part of our competency, we need to understand which components of the bicycle have the highest likelihood of failing, and what the impacts of their failure are. So we do this kind of risk analysis to create an accurate risk profile and potentially introduce mitigation plans if we discover that a component introduces unacceptable levels of failure.

### Causality

The next step is to determine causality. Why are these failures occurring? In the real world you might systematically determine causality by:

- Determining the design deficiency that results in the failure mode
- Determining a manufacturing process deficiency
- Determining a user’s failure to perform a task

These 3 span a wide variety of potential root causes, and it’s common to separate out an FMEA into design FMEAs, process FMEAs, and use case FMEAs in order to organize the risk analysis better. For our example, we’ll only focus on design deficiencies.

![FMEAs](FMEAs.png)
*FMEAs*

Let's identify some causes of failure. A reason the drivetrain might fail to convert rotational motion into horizontal motion is because the _pedals detach_. Brake failure might occur because the _brake cable snaps_, or the _brake disc overheats_. Finally, the frame may fail because the _seat tube or head tube detaches_.

---

<span style = 'color: green; font-size: 32px;'>**Component:** Drivetrain</span><br>
<span>**Function:** Convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Drivertrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'color: green; margin-left: 80px;'>**Cause:** Pedals detach</span><br>

<span style = 'color: red; font-size: 32px;'>**Component:** Brakes</span><br>
<span>**Function:** Convert kinetic energy into heat</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Brakes COMPLETELY fail to convert kinetic energy into heat</span><br>
<span style = 'color: red; margin-left: 80px;'>**Cause:** Brake cable snaps</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Brakes PARTIALLY fail to convert kinetic energy into heat</span><br>
<span style = 'color: red; margin-left: 80px;'>**Cause:** Brake disc overheats</span><br>

<span style = 'color: blue; font-size: 32px;'>**Component:** Frame</span><br>
<span>**Function:** Support the cyclist</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support cyclist</span><br>
<span style = 'color: blue; margin-left: 80px;'>**Cause:** Seat tube detaches</span><br>
<span>**Function:** Support the components of the bicycle</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support components</span><br>
<span style = 'color: blue; margin-left: 80px;'>**Cause:** Head tube detaches</span><br>

---

### Effects of Failure

We're almost there! The last step is to identify the **effect** of each of our failure modes. These failure modes are once again written generically, because once we get deeper into this analysis, we will want to make it easy to connect multiple failure modes to the same end effect. This will allow us to make interesting insights at the end of the analysis about how many end effects are the results of certain types of failures.

For now though, for the drivetrain component, the effect of being unable to convert rotational motion into horizontal motion is that the _cyclist cannot accelerate the bicycle_.

For the brakes, the effect of being unable to completely convert kinetic energy into heat is that the _cyclist cannot decelerate the bicycle_. The effect of only being able to partially convert kinetic energy into heat is that the _cyclist's ability to the decelerate the bicycle is reduced_.

Finally, for the frame, the effect of being unable to support the cyclist is that the _cyclist falls from the bicycle_. The effect of being unable to support the components is that the _components detach from the bicycle_.

---

<span style = 'color: green; font-size: 32px;'>**Component:** Drivetrain</span><br>
<span>**Function:** Convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Drivertrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 80px;'>**Cause:** Pedals detach</span><br>
<span style = 'color: green; margin-left: 80px;'>**Effect:** Cyclist cannot accelerate bicycle</span><br>

<span style = 'color: red; font-size: 32px;'>**Component:** Brakes</span><br>
<span>**Function:** Convert kinetic energy into heat</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Brakes COMPLETELY fail to convert kinetic energy into heat</span><br>
<span style = 'margin-left: 80px;'>**Cause:** Brake cable snaps</span><br>
<span style = 'color: red; margin-left: 80px;'>**Effect:** Cyclist cannot decelerate bicycle</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Brakes PARTIALLY fail to convert kinetic energy into heat</span><br>
<span style = 'margin-left: 80px;'>**Cause:** Brake disc overheats</span><br>
<span style = 'color: red; margin-left: 80px;'>**Effect:** Cyclist's ability to decelerate bicycle is reduced</span><br>

<span style = 'color: blue; font-size: 32px;'>**Component:** Frame</span><br>
<span>**Function:** Support the cyclist</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support cyclist</span><br>
<span style = 'margin-left: 80px;'>**Cause:** Seat tube detaches</span><br>
<span style = 'color: blue; margin-left: 80px;'>**Effect:** Cyclist falls from bicycle</span><br>
<span>**Function:** Support the components of the bicycle</span><br>
<span style = 'margin-left: 40px;'>**Failure Mode:** Frame fails to support components</span><br>
<span style = 'margin-left: 80px;'>**Cause:** Head tube detaches</span><br>
<span style = 'color: blue; margin-left: 80px;'>**Effect:** Components detach from bicycle</span><br>

---

### Subsystem DFMEA and Mitigations

We made it! Great job for sticking through that. We slogged our way through a system DFMEA and made a pretty basic, but useful framework to run with and expand upon. Before we wrap up, let's take a look at a completed subsystem DFMEA so we can see how it has its own recursive definition of all these elements as well. We will focus on the _Pedals_ sub-component here.

<span style = 'color: green; font-size: 32px;'>**Drivetrain Component**</span><br>
**Sub-Component:** Pedals<br>
<span style = 'margin-left: 40px'>**Function**: Translate force of legs to rotational motion of crankset</span><br>
<span style = 'margin-left: 80px'>**Failure Mode:** Pedal detaches from mounting point</span><br>
<span style = 'margin-left: 120px'>**Cause:** Precession causes pedals to loosen </span><br>
<span style = 'margin-left: 120px'>**Effect:** Drivetrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 120px'>**Mitigation:** Reverse-threaded pedal mount</span><br>
<span style = 'color: lightgrey'><br>
**Sub-Component:** Chain<br>
<span style = 'margin-left: 40px'>_Function_: Translate force from crankset to force in sprocket</span><br>
<span style = 'margin-left: 80px'>**Failure Mode:** Chain snaps</span><br>
<span style = 'margin-left: 120px'>**Cause:** Coarse particles wear down links</span><br>
<span style = 'margin-left: 120px'>**Effect:** Drivetrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 120px'>**Mitigation:** [none]</span><br>
**Sub-Component:** Crankset<br>
<span style = 'margin-left: 40px'>_Function_: Translate rotational motion of pedals to linear motion of chain</span><br>
<span style = 'margin-left: 80px'>**Failure Mode:** Crank arm detaches from mounting point</span><br>
<span style = 'margin-left: 120px'>**Cause:** Precession causes crankset to loosen</span><br>
<span style = 'margin-left: 120px'>**Effect:** Drivetrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 120px'>**Mitigation:** Reverse-threaded crank mount</span><br>
**Sub-Component:** Rear sprocket<br>
<span style = 'margin-left: 40px'>_Function_: Translate linear motion of chain to rotational motion of wheel</span><br>
<span style = 'margin-left: 80px'>**Failure Mode:** Sprocket teeth wear down</span><br>
<span style = 'margin-left: 120px'>**Cause:** Coarse particles wear down teeth</span><br>
<span style = 'margin-left: 120px'>**Effect:** Drivetrain fails to convert rotational motion into horizontal motion</span><br>
<span style = 'margin-left: 120px'>**Mitigation:** Add holes to sprocket to better retain grease</span><br>

Recall that a good FMEA should tell a good story. In this case, the story being told is that we have a sub-component called the pedals, whose primary function is toc translate the force of the legs pushing down on them into rotational motion in the crankset. One way this function can fail to occur is if the pedal detaches from its mounting point on the crank arm. A reason this might occur is because of precession, which is a phenomenon by which rotational motion causes a screwed object to unscrew itself from its mounting point. Fortunately, a very simple way to prevent this from occuring is to reverse-thread one of the pedal mounts. That way, when the cyclist pedals, they tighten the pedal against the crank arm, as opposed to loosening it.

Of course this is just an example, and any competent bike manufacturer will include this feature from the start. But we're new to bike manufacturing and learning along the way! Good thing we did some risk analysis to figure this out ahead of time.

## Summary

With this exercise, we have developed a rudimentary FMEA, but more importantly we have developed _a framework to think about any engineering project in terms of risk_. This can be a very powerful tool especially in software.

Remember that your code base often contains a LOT of code that no one on your team wrote. This can be in the form of NPM modules or other ecosystem dependencies. In the biz, this is sometimes called Software of Unknown Provenance, or **SOUP**. It's just as important to understand what's in the SOUP as it is to understand what's in your own code.

A great interface document for understanding what's in the SOUP that might make you sick is an FMEA made by the provisioner of the SOUP. When that's not available, or another equivalent that describes potential failure points in the code, then you really ought to be checking out what's in those dependencies to make sure you're not introducing unknown amounts of risk into your project. It is common for dependency developers to provide an automated test suite, which is helpful to study in order to identify any blindspots in their testing that might impact the behavior of your program.

## What's Next?

Now that we have created a rudimentary FMEA, what's next?

- We should introduce a mathematical framework that allows us to compute probabilities of failure and severities of effects.
- We should also organize our efforts to burn down risk by focusing on components with the highest probabilities of failure and/or severities of effects

By introducing some math, we can start to visualize our risk burndown in much more interesting ways.

![Sankey Unweighted](sankey-unweighted.svg)
*Unweighted Sankey diagram*

For example, here is a [Sankey diagram](https://en.wikipedia.org/wiki/Sankey_diagram) I created. This type of chart is called a flow diagram, where the width of each connection represents a vaguely-defined "riskiness" measure that I've just made up. You could think of this as some sort of product of `probability of failure` x `severity of failure`, broken down by component. In this naive example, I'm assuming that every component contributes equally to this made-up "riskiness" measure.

![Sankey Weighted](sankey-weighted.svg)
*Weighted Sankey diagram*

But by creating a mathematical framework for our components to interact with, we can start to come up with a more interesting diagram. This diagram can now tell us which particular components and sub-components contribute the most to our overall risk profile. With this information, we can decide where our efforts are best directed in order to reduce the overall risk profile of the project.

For example, here at Ashwin Bicycle Industries, we _know_ what we're doing when it comes to drivetrains and brakes. That's old hat to us. But bicycle _frames_? That's new, and difficult. There's a lot of risk involved in our current techniques. So we have some extra work to do to burn down the risk associated with our brittle bicycle frames.

And we can clearly see that in the above diagram! The bicycle frame component has an overall risk value of 150, representing nearly half of the risk associated with our bike in total. Program managers can use this information to better allocate some extra resources to the parts of the project with the most risk.

## Conclusion

Understanding the full risk profile of your project can be extremely lengthy. In regulated industries there are entire groups dedicated to this single task. Depending on the type of development you're doing, it's probably not necessary to construct an FMEA for _every_ single component of your project.

Perhaps on the next project you start, you could take some time up front to identify a few critical components of your application that might benefit from risk analysis. You'll probably find that:

- You understand your code base in more detail than before
- You're able to communicate how long a bug fix might take with more accuracy
- You're able to identify future issues before they manifest themselves in a production environment

_This article was originally written for the [engineering blog](https://engineering.deptagency.com/risk-management-framework-software) at DEPT®, a technology consultancy_
