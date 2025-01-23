import streamlit as st
import cohere
# Title for the app
#st.title("IEM AI")
# Center the title using Markdown and HTML
st.markdown("<h1 style='text-align: center;'>IEM AI</h1>", unsafe_allow_html=True)

# Center the logo
#st.markdown("<div style='text-align: center;'><img src='https://github.com/SanjaiSaminathan/IEM-AI/blob/062cf74f7f29357febb25744323cdc2bc59d1435/logo.png' width='150'></div>", unsafe_allow_html=True)
# Add the logo at the top
#st.set_page_config(page_title="IEM AI", layout="centered")
st.image("logo.png", width=150)  # Adjust `width` as needed

# Input box
user_input = st.text_input("Enter the Question:")

# Button to process the input
if st.button("Process"):
    
    # Set your API key
    co = cohere.Client("vqTej7Mv9k4DZOUnzVrciquxeZail4uhkt1roip3")

    # Define context and question
    context = """
    1. We solve all your building maintenance challenges Quickly, Affordably, and Efficiently FM-made simple IEM simplifies the complexity of facilities management, allowing you to easily control the risks and turn your buildings into business enhancers. We specialize in redefining estates from mere cost centers to pivotal business enablers. With extensive expertise in facilities management, we empathize with the challenges of accountability in the absence of streamlined processes. We recognize the burden of risk management overshadowing opportunities for meaningful business impact.


    2. Business impact. What We Do
    BUILDING PROJECTS
    We carry out all aspects of building projects, from design to delivery, to handover
    TECHNICAL CONSULTANCY
    We provide technical consultation and support, across all aspects of your estate
    PLANNED AND REACTIVE MAINTENANCE
    We deliver hard services, covering planned, remedial, and reactive maintenance, specializing in compliance.

    3.   Why work with IEM?
    NO CONTRACT
    No long-term obligation
    We are only as good as our last job Gives you a flexible solution with no fixed-term commitment
    FREE CAFM SYSTEM
    Reduces Costs Centralised Maintenance Control and Compliance documentation management
    Total visibility in one place
    REGIONALISED SUPPLY CHAIN
    Timely and quick response times
    More efficient sustainability
    Supporting local contractors


    4. Supporting local contractors
    COMPANIES WE HAVE PROUDLY SERVED INCLUDE:
    Client Chatham House
    IVC Evidensia
    Stonegate Pub Company
    Bvlgari
    Logo Cox Automotive Brand Font Vector Graphics Png Favpng
    Nhs  1
    Knightsbridge  Blue
    Dough And Co
    Arnold Clark
    Rockhurst
    Motorpoint
    Quills Group
    
    
    5. How facilities management can future-proof your business
    Strategic facilities management is a powerful tool for those that know how to use it. For many businesses, estate management is often reactive and fails to develop assets and add value to portfolios.
    
    The global pandemic has been hugely disruptive in the field of estate management. First, many premises were abandoned – virtually overnight – for an unknown period of time. Now, as we plan a return, organisations are having to make drastic changes to the way they use their sites in order to keep staff safe. Designing resilience into assets can not only protect them but aid the organisation as a whole.
    
    This must start with an in-depth understanding of the estate, it’s strengths and its weaknesses. For many, hard elements of FM have been hugely challenging over the previous months since they are designed to function with the building at near full capacity.
    
    Failure to manage this situation can result in a lack of compliance. At worst, this can lead to dangerous health outcomes as was seen with an outbreak of Legionnaires’ disease earlier this year. Understanding risk allows potentially costly and hazardous problems to be avoided.
    
    Once the fundamental needs of the organisation are met by its estate, attention can be turned to increasing the value of assets. Sites and premises should be viewed in terms of their potential. The upkeep of under-utilised sites is a resource drain.
    
    Instead, these areas should become a focus for redevelopment. Real estate should add value to the organisation through by enhancing the safety and productivity of a site.. Portfolio optimisation is a key way of financially streamlining an organisation, providing a buffer for unexpected spends or greater potential for investing into development.
    
    An area garnering increasing attention is the creation of a workplace that supports the productivity and wellbeing of employees. Future-proofing is about embracing change. The way we work will continue to evolve, especially as we continue to recover from the pandemic.
    
    Spaces should be designed to allow for agile working and changes in working style. The most flexible thing in a space is never the furniture, nor the walls. It’s the people. Space should encourage movement, creative work, and facilitate safety.
    
    The space should also reflect and encourage a strong workplace culture. A close-knit workplace culture is important for keeping staff motivated and engaged even when times are difficult. Staff that feel supported and at home in their workplace will be more loyal.
    
    Finally, the sustainability of the workplace will be under ever greater scrutiny in the coming years. With many of the greatest challenges business face, including the global pandemic, traced back to unsustainable practices, the pressure will be on everyone to do better.
    
    Estate managers can save on costs and improve the reputation of an organisation by implementing sustainable practices. From insulation and waste disposal to buying furniture made of more eco-friendly material, the possibilities are endless.
    
    The role of the estate manager is both to be a creative problem solver and a visionary for the potential of the portfolio. Those with a strong understanding of estate management and how it aligns with the organisation’s priorities have a powerful tool at their fingertips.
    
    
    5. Meet the Team: Alistair Scott
    What is your role at IEM and what does it involve day to day?
    I am responsible for the day-to-day operations of the company and all the technical support elements. This involves making sure the team have the right tools, equipment and support to do a great job. By doing this, the team are then enabled to get the best out of themselves. I don’t like micro-management, so I like to agree success criteria up-front with the team and then allow them to do it their way.
    
    I enjoy getting involved in the fulfilment of the large technical projects and ensuring they are executed correctly, to a high standard and on time. A lot of my time is also spent on maintaining and growing client relationships, ensuring the customer experience is always to a high standard.
    
    How did you find your way into estate management? (Tell us a bit about your background)
    I was trained as an engineer in the military. Concurrently, this is where I grew as a leader, deploying and leading teams when training or in operation. This taught me how to lead, manage, and develop a diverse group of individuals. I molded them into a highly effective team that was capable of delivering a variety of complex projects on a timely basis and across a variety of environments.
    
    It doesn’t surprise me that there are a lot of ex-military personnel working in facilities management as there are many traits that are similar.
    
    I got involved initially from the engineering angle, as I understood electrical, mechanical, and electronic systems. On top of that, I had the leadership competency to put people in the right place, with the right piece of equipment to do the job first time….which at the end of the day is facilities management.An estate manager using a tablet during a site visit
    
    What is your favourite thing about your job/the industry?
    I absolutely love what I do. What really excites me is that no two days are the same. It’s a really diverse industry when it comes to all the different problems that come up on a daily basis. Therefore, you're constantly thinking and challenging yourself. It keeps your brain moving and allows you to stay engaged. You naturally feel ecstatic when you do something good for someone. We're not going in and smashing the place up, we're going in to make things work, adding value to businesses and buildings and landlords. For me, this is really exciting and my favourite part of the job.
    
    How could the industry be improved?
    The biggest challenge we’ve faced as an industry is people’s perspective of us, and their understanding of what we offer. However, I think we’ve already started seeing improvements in this area. Years ago, businesses went to large FM companies to do everything for them. Now, companies are realising that having the right people with the right skill set within the facilities management sphere, is more of a benefit than just going to a general FM provider. It's like the high street, people are flocking back to local butchers or bakers because it’s more personal and better quality. FM is no different, people like going to specialists within their field but they also want that personal touch.
    
    What are your key predictions for/the biggest issues facing the estate management industry over the next year?
    Technology is really being pushed and for the right reasons. However, I have on a few occasions added a cautionary warning into going down this route. Overall, I really like IOT, especially if utilised correctly. It can give you plenty of warning if things go wrong, telling you if something’s going to fail, and can be really useful for a range of services. However, it’s important we still remember the basics and not rely heavily on technology. A trend I’m seeing is technology taking so much of the limelight that the fundamentals are being forgotten. As much as advancements in technology is a good thing, the basics can’t be forgotten. It all links back to simplicity, you don’t always need lots of advanced equipment and the latest tech, just the right tools and the right people.
    
    What is your biggest passion/favourite hobby outside of work?
    A Formula 1 car on the race trackI am a massive motor-sport fan. I follow all genres and types, whether it be road cars, British Touring Cars, or Formula 1. I am also heavily involved with amateur race driving and even motorbikes. If it’s motorized and fast, I love it.
    
    Gone are the days I really get involved in the tinkering element, but the driving experience and that team ethic of everybody in a team working towards a common goal, as well as achieving that goal on time, is what I still love and have taken into the business arena.
    
    My other major passion is cooking. For me there is nothing more relaxing than cooking a meal for family and friends, with everyone sitting around a table on weekends, chatting and enjoying the experience. These are those special moments that we missed during Covid times, that I can’t wait to start doing again.
    
    6. Why support for facilities managers is essential as buildings reopen
    One of the side effects of the pandemic, working from home and the workplace revolution is that we all have a greater appreciation of the impact of buildings on our mental health and wellbeing. But what about the mental health of those charged with managing buildings as they reopen?
    
    Many businesses may look to adopt a hybrid work model post-pandemic, but the reality is that most buildings are on track to be fully reopened in June when the Covid restrictions end. Many of these spaces have been dormant or below occupancy for more than a year and compliance might have fallen by the wayside.
    
    Ensuring buildings are safe to reopen is not just about cleaning and hygiene. It’s about ensuring that all aspects are compliant, and that duty falls to estate managers. That level of accountability is a big burden and will undoubtably be the cause of much stress for those individuals.
    
    An anxious return?
    
    It’s quite clear that the onus is on employers to help building occupants feel supported in their mental health, and estate managers have a big role to play.
    
    There will be plenty of people that are excited to get back to the office, but there will be just as many that are anxious about the return.
    
    Business leaders too will be anxious. They want to ensure the safety of their employees, clients, and customers. They also have a financial risk to consider. If a building fails compliance, that might lead to a fine or the space being shut down. That could be highly disruptive to the business.
    
    Estate managers must manage these risks and communicate with leadership and building users how and when they have been mitigated. It’s a big weight to carry and we businesses must ensure that their estate managers have the support they need – not just through the tools they need to do their jobs, but on the wellbeing side too.
    
    Supporting estate managers
    
    Estate teams should already be working in close consultation with other senior leaders. Since the pandemic struck and the role of the building was amplified, many estate managers have found themselves to have an elevated voice in the business. Now is the time to capitalise and ensure that this remains the case long after the pandemic.
    
    Estate managers should share how and why they are managing various tasks, from compliance to lighting, and water safety to energy management. For their part, business leaders must do all they can to support them in achieving their goals.
    
    This could include the creation of an up-to-date asset list; an audit of building condition; compliance inspections and assessments; prioritising projects; and the delivery itself.
    
    This can be a hugely demanding workload for a team, let alone a one-man band. In many cases it can be beneficial to partner with an expert consultant to help manage one of more areas of estate management. Business leaders can support their teams by being open to this option.
    
    This is not just a ‘nice to do’. This is essential in supporting the mental health of estate managers, and in turn the business.
    
    We offer a range of estate management services that will support your business and its employees. Contact us today to discuss how we can support your estate management.
    
    
    7.  IEM founder Alistair Scott bids to join IWFM board
    IEM founder Alistair Scott has nominated himself to join the board of the Institute of Workplace and Facilities Management (IWFM). The IWFM, formerly the British Institute of Facilities Management, was formed in 1993 and exists to “promote excellence among a worldwide membership community of around 14,000 and to demonstrate the value and contribution of workplace and facilities management more widely”.
    
    The IWFM board consists of 13 members, six of which are volunteers who must hold professional membership within the Institute. Alistair has applied for the role of non-executive director as he hopes to use his extensive experience to help the board meet and exceed its objectives.
    
    Voting is now open. All members of the IWFM at member grade and above are eligible to vote and we’d love your support – you can vote for Alistair here.
    
    Alistair Scott’s candidate statement
    I am a certified mechanical, electrical and electronic engineer and have more than 25 years’ experience in technical engineering and senior facilities management roles. Throughout my career I have witnessed the good and the bad of facilities management, as well as seeing many opportunities for improvement. Through my experience and expertise, I truly believe that I can add significant value to the IWFM organisation.
    
    As the founder of my own FM company, Integrated Estate Management, I am fully aware of the need for strong strategic direction, setting and measuring objectives, and astute financial management. My engineering and military background has given me excellent leadership skills to complement the business acumen that I have developed in the last two decades.
    
    I look forward to taking an active role on the board, sharing my expertise and helping to drive the IWFM towards its objectives. I have held numerous board positions and operated across multiple industries, including the following companies, Gatwick Airport, BAA, Liquid Capital and AkzoNobel (ICI) and Cloudfm. I understand the commitments and responsibilities that come with being a board member and am ready to support the IWFM.
    
    I have a distinct passion to make this industry more appealing, simple to understand and desirable to work in. Recognition of the facilities management sector has grown tremendously in the last 18 months, and I believe we must capitalise on this opportunity.
    
    The IWFM has a vital role in this, and I am excited to play my part.
    
    I am actively engaged in the industry and am always looking for ways to promote FM. As an FM coach and mentor, I have heard many of the concerns and frustrations from people within the industry and am looking forward to working on the board to improve the industry and add value.
    
    I am also involved with the Women in Construction organisation and share my expertise with the industry through comments and articles in leading trade titles such as Facilitate, FMJ and iFM.
    
    I ask for your vote so that I can support the IWFM as it enters an exciting new era.
    
    Vote for Alistair
    If you are an IWFM member, please cast your vote for Alistair.
    
    
    8. The future is bright; the future is simple
    Facilities Management shouldn't be this complicated!
    
    When IEM was founded, we did not want to perpetuate the confusion and complexity often associated with FM, so we made the decision to keep things simple.
    
    There were various reasons for this thinking, but the most important of these was the bad reputation that the industry had acquired, mainly due to its somewhat chequered history.
    
    According to Reuters, one of the primary reasons FM businesses have struggled in recent years (Carillion and Interserve spring to mind) is the continuous hamster wheel of signing long fixed-rate contracts at un-sustainable pricing.
    
    Complicating the services offered to clients makes it easier to hide the real cost and mask the value customers are getting.
    
    Simplifying complexity is a skill that most great businesses and leaders possess, but it is sometimes missing in FM.
    
    "Simple can be harder than complex. You have to work hard to get your thinking clean, to make it simple. But it's worth it in the end, because once you get there you can move mountains" Steve Jobs
    
    As the world becomes smaller, the ease with which businesses can get information into the marketplace becomes even easier. However, the need for quality content that stands out becomes ever more necessary.
    
    Selling service-driven products is challenging, especially in a world of so much noise, quality content and competition. When trying to justify a price-point, expensive complex products are usually perceived as more merited than simple ones.
    
    Successful organisations and leaders are highly skilled in simplifying this complexity, instead of "complexifying” simplicity.  However, if you get it wrong, this can confuse your customers, who nod their heads politely but have no clue how you will ease their pain points.
    
    Clarity and simplicity
    
    "If you can’t explain it simply, you don’t understand it well enough" Albert Einstein
    
    Any industry focused on selling to the lowest bidder will always have underlying challenges, especially if that industry relates to services. The way many businesses overcome this issue is through "Bundling" or giving perceived value. After all, it is easy to compare apples with apples (hourly rate of jobs, materials and length of time) but much harder to compare the more subjective elements (quality, management fees and administrative support.)
    
    FM has always been an industry famous for its acronyms and hidden costs; that’s why there is a need for clarity and a much more simplistic approach. Good FM companies will sell real features and services that customers genuinely need, rather than perceived value, due to "Bundling" features that clients will never use.
    
    One of the main challenges the FM industry has had, is that they have to come in at the lowest price and give the perception of more added value. The FM industry needs to understand the power of clarity and simplicity.
    
    When building a sustainable business, concepts, jargon and complex features should never be at the expense of customer benefits.
    
    The next few years should bring a shift from the complicated world of hidden features and acronyms that nobody understands, to a drive for removing complexity and replacing it with simplicity.
    
    The Future is bright
    
    Outsourced providers will need to add more value than before. Increased spending budgets to get businesses up and running as soon as possible will create more business opportunities.  FM companies that can adapt quickly, focus on the basics, without the bells and whistles, whilst helping customers prioritise, are the most likely to flourish and grow.
    
    Other reasons why 2021 will be bright for the FM industry include:
    
    Cost reduction may be necessary, but organisations will also need to free up more funds to get their estates trading in super-fast time.
    With many buildings closed for so long, there will need to be urgent investments in Health and Safety, including compliance checks.
    FM/Property Managers will suddenly have more exposure and be at the forefront of strategic decision making.
    IoT and AI advances will make the industry sexier, especially the drive towards predictive and preventative maintenance - however, this may need to be put on hold for a short while, as businesses open safely and get their basics right first.
    Employees will probably want to get back to their workplaces and interact face to face with their work colleagues once more, and this will be a crucial part of facilities teams’ activities over the Spring and Summer months.
    There will be a level of urgency not seen for many years, so the demand for services will be very high.
    If FM companies get things right and make it easier for customers to attain more value, the next 12-24 months could be one of the most exciting times in history for the industry. Getting estates up and running in a post-covid world, will bring many opportunities for FM businesses to grow and for clients to build workplaces that will be business enhancers, not just cost centres.
    
    We were set up with the goal of simplifying estate management. Contact us today to discuss how we can support your business.
    
    9. 5 key considerations for facilities management when reopening a building
    The current lockdown means that many workplaces have become vacant again, or at the very least continue to be vastly under-occupied. Though it may feel like a return to normal is a long way off, estate and facilities managers must prepare now for that time.
    
    When the restrictions do ease, a lot of businesses may see a clamour from employees who want to get back to their place of work. This process cannot be rushed and estate managers have a vital role to play in ensuring that a workplace is ready to be occupied again.
    
    There are of course numerous things to consider to get a workplace ready to reopen. Here are five of the most important.
    
    Hygiene
    This may seem obvious, but it’s absolutely critical to stay on top of hygiene. This includes keeping updated with the latest information from the Government and health bodies, as well as implementing strong hygiene processes at a site. Estate managers should act as a key consultant to organisations. Even though we are ten months into the pandemic, it cannot be assumed that all building occupants will know or follow the best hygiene practices, so signage and consistent communication with all occupants is a must.
    HVAC
    We know that the virus is increasingly airborne. HVAC systems must be assessed and adapted to ensure that they provide a strong defence against airborne transmission. This can include the type of air filters used, the frequency they are changed and the percentage of outside air pumped into a building. Where possible, windows should be left open to increase ventilation.
    Compliance
    Compliance covers everything from fire risk to electrical, and legionella to asbestos. In buildings that have spent any time vacant or with reduced occupancy, it’s highly likely that checks will need to be made before full occupancy to avoid both fines and health and safety breaches. Take water systems, for example. Many are designed under the assumption of regular flushing due to full a site being fully occupied. Times of irregular flushing can provide an opportunity for bacteria to flourish, which in the worst case scenario can lead to an outbreak of legionella. Estate managers should assume nothing is compliant as they prepare a site for reopening.
    Asset management
    Even the most up-to-date asset registries will need going over with a fine tooth comb ahead of a building reopening. It’s likely that the condition of many assets will have changed in the last year. For businesses without an understanding of its assets and their condition, this represents an opportune time to carry out an in-depth survey. This will also be an important step in ensuring compliance.
    Project management
    The sheer numbers of estate management tasks can be daunting for even the most experienced estate managers, let alone for small and medium sized businesses that may not have the in-house resources to cope. It’s worth partnering with a project manager to handle the process. The expertise is invaluable and any money spend will be made back many times over in workplace optimisation and the avoidance of fines for breaches of compliance.
    
    The IEM team is here to help you manage your estate. Whether you need a range of services, project management or simply a chat about how to transform your estate into a business enhancer, we can help out. Check out our Five Point Plan or contact us to find out more.
    
    
    10.  How to make facilities management simple and effective
    Facilities management, at its heart, is about looking after things. It is a vast role and may appear inherently complex, but it does not need to be difficult. By simplifying each of the elements of estate management, it is possible to create a streamlined and cohesive approach.
    
    For many, the instinct is to outsource to a large facilities management (FM) organisation with expertise in estate management. However, this isn’t an option for many smaller and mid-sized companies.
    
    Yet opting for the cheapest option on the market risks shelling out for a service that doesn’t do justice to the estate. For those managing their estate themselves, it can feel like an overwhelming challenge just to meet compliance measures and the time and resources this requires can distract from transforming the estate into a genuine business asset.
    
    In virtually every sector, organisations are looking to simplify and streamline their processes. This is possible with estate management too. By breaking the process down, it becomes easier to address each of the core elements of management, meet key targets, and understand priorities.
    
    Understanding what assets an estate possesses should be the key objective of an estate manager. Location, condition, life span, and economic value should all be identified. This should then be followed by a more in-depth investigation into the condition of those assets. Here, risks can be identified and precautions taken.
    
    Ensuring compliance is vital in any estate; non-compliance can come with unplanned costs and long-term damage to reputation. An understanding of asset condition allows compliance requirements to be met.
    
    From here, an organisation is in a position to plan for the future, begin forecasting capital expenditure and planning for tenders. A five-year plan can be produced with key compliance and business critical remedials prioritised according to risk. Finally, improvements and projects can go ahead, be they adjustments and refurbishment or major upgrades.
    
    By creating a step-by-step process, each element of estate management becomes manageable and vital aspects won’t be overlooked. Once your organisation understands precisely which areas of the estate need work and what needs doing, you are in a much better position to look for the best experts for the job. Simplifying the process makes it both transparent and accessible.
    
    While the remit of estate management is extremely broad, it is an opportunity to take a holistic view of the organisation’s assets. Once the process has been demystified, it can be an opportunity to build on what the organisation has in order to create an estate that reflects the business culture and feels like a home for its people.
    
    Excellence in estate management requires strategic thinking and continuous evaluation of the estate. For those new to this approach, there is a big learning curve, but streamlining the process makes it accessible to all.
    
    
    11. About IEM
    At IEM, our primary objective is clear: to transform inefficient spaces into productive environments, optimising your buildings to support your strategic goals.
    
    Say goodbye to cost centres and hello to business enablers with IEM's innovative approach to facilities management.
    
    We understand the frustrations of navigating the risks and everyday challenges of estate management, which can detract from your ability to contribute positively to your business.
    
    Integrity, reliability, simplicity, and transparency are the cornerstones of our approach.
    
    CONTACT US today to discover how we can streamline your facilities management processes.
    
    As facilities management experts, we extend our services to include project delivery, regardless of whether we provide the ongoing services or not.
    
    12. THE IEM STORY
    Alistair Scott, the driving force behind IEM, brings over 25 years of experience in technical engineering and senior facilities management roles. A certified mechanical, electrical, and electronic engineer, Alistair's journey began in the British Army, where he served for 14 years within the Royal Electrical Mechanical Engineers (REME), rising to the rank of Captain. During his military service, Alistair excelled as a mechanical aircraft technician, ultimately attaining the esteemed position of Engineering Officer. Transitioning from the military to the civilian sector, Alistair embarked on a global career in the facilities management (FM) industry. He held pivotal board positions at renowned organizations such as Gatwick Airport, BAA, Liquid Capital, and AkzoNobel (ICI), gaining invaluable insights and expertise along the way. Driven by a passion to revolutionise the FM industry and frustrated by its unnecessarily complex nature, Alistair founded IEM. With a commitment to simplifying processes and making a meaningful difference, Alistair leads IEM in its mission to deliver innovative, efficient, and sustainable facilities management solutions.
    "I have worked in senior FM roles across numerous industries and the common factor in them all was the daily complexity. I believe that facilities management should be simple to understand and deliver - that's why I founded IEM. I want to help organizations better understand their buildings, have more control over them and transform their estates into business enhancers."
    
    13.
    Our work
    IEM was founded to make facilities management simple, transparent and effective. To achieve this, we created our Five Point Plan. The plan covers end-to-end facilities management: Know your assets;
    Understand your condition;
    Control your compliance;
    Package your priorities;
    Manage your delivery.
    The plan can be tailored to meet your exact requirements – we can work on one or all five points with you. Find out more about our Five Point Plan. We have a nationwide network of certified engineers that have expertise in every facet of estate management, including electrical, mechanical, water systems, compliance, lighting and HVAC. See the full list of services we offer on our services page. IEM has experience in a range of sectors, including commercial, retail and warehousing. See the full list of our sectors here.
    
    Scottys little Soldiers
    Visit Scottys little Soldiers Website
    Care After Combat
    Mission Motorsport
    IWFM
    Veterans Can
    Bronze Military Covenent
    
    14. ACCREDITATIONS
    
    IWFM
    Safe Contractor Approved
    Gold With Dark Font Transparent1
    BESA Associate PNG
    Qualitas IMS 45001 Certified  (1)
    Qualitas IMS 9001 Certified
    Qualitas IMS 14001 Certified
    Principal Safety
    Best Company to work For "FM awards2024"
    
    15. Five Point Plan
    The plan is designed to be flexible and to fit your needs. You can pick and choose which elements you want IEM to help with and we'll work seamlessly with in-house services and other contractors.
    
    1. Know Your Assets
    According to Compare Soft, an effective asset register can have an impact on your revenue and cash flow by 5 – 18 per cent. We identify your assets and their location, condition, life span and economic value. We leave no stone unturned in creating an up-to-date register.
    Identify assets and location
    Condition
    Life span
    Economic value
    
    2. Understand Your Condition
    Evaluating the condition of an estate is a daunting prospect. We survey your buildings, identify construction and repair requirements, identify any risks and collate the data into a user friendly report.
    Survey your buildings
    Identify construction and repair condition
    Identify your risks
    Collate data
    
    3. Control Your Compliance
    The cost of health and safety fines is routinely higher than the cost of compliance. Businesses also have a duty to protect their employees and customers. We assess your current compliance position, check it against the latest legal guidance, carry out compliance inspections and categorise remedial and improvement actions. The end result is you will be fully compliant and have an easy way to manage compliance moving forwards.
    
    Assess current compliance position
    Legislative guidance
    Compliance inspections
    Categorise remedial and improvement actions
    
    4. Package Your Priorities
    With a full understanding of your estate, we’ll work with you to identify and address your priorities. This includes producing a plan for up to five years ahead, forecasting CAPEX expenditure, balancing priorities versus statutory requirements and assisting with tender production.
    
    Produce a 1-5 year plan
    Forecast your CAPEX expenditure
    Organise priorities overlayed against statutory requirements
    Tender production
    
    5. Manage Your Delivery
    We can take the lead role in delivering your program across one or multiple sites. We also offer construction, design and management support and deliver major upgrades and refurbishment work through our 2,500 strong nationwide network of engineers.
    
    
    Programme or project
    
    CDM support
    
    Individual or multi-site discipline delivery
    
    Deliver major upgrades and refurbishment works
    
    
    
    6. Frequently Asked Questions
    What is facilities management?
    Facilities management encompasses every aspect of a property, including electrical, water, lighting, health and safety, maintenance and compliance. It's also commonly referred to as estate management.
    
    Are your contractors certified and monitored?
    Does IEM just do repairs?
    IEM deliver all aspects of total building maintenance from planned, reactive to technical projects.
    
    Do you offer 24-hour (24/7) support?
    Yes, we are available 24/7, feel free to call any time for assistance and support
    
    Why did you come up with "The 5-point plan"?
    IEM was created in order to simplify the complexity of estate management, the 5-point plan is the framework that underpins our philosophy
    
    Why does IEM believe simplicity (removing the complexity) is so important?
    Through our extensive estate management experience, we identified that the complexity within maintaining a building leads to in-action, frustration and risk.
    
    Why is facilities management important?
    There are numerous benefits to effective facilities management. It is essential to remain compliant across all facets of an estate to avoid fines and to ensure that all occupants are safe while on the premises. Strong estate management practices can also transform a property from a risk to an asset. A well maintained estate can also be a big driver towards creating a productive working environment.
    
    What services do IEM provide?
    We provide every element of estate management, from asset management through to programme delivery. We have a nationwide network of more than 2,500 engineers that can be called upon at a moment’s notice to carry out any job.
    
    Can I pick and choose what services I need from IEM?
    Absolutely. You can engage us for our entire Five Point Plan or we can tailor a unique plan just for your estate. We will work seamlessly with your in-house team or other contracted services.
    
    How much does facilities management cost?
    This can vary depending on the size of your estate and the services you require. Contact us to find out more.
    
    Tel: 0203 772 4188
    info@integrated-em.com
    
    31, Facilities management services
    REACTIVE AND PROACTIVE MAINTENANCE
    
    At IEM, we specialise in both reactive maintenance to swiftly address immediate issues and proactive maintenance strategies to keep your facilities operating smoothly. Whether you need urgent fixes or planned preventive maintenance (PPM) to prevent future problems, we have the expertise to meet your needs. What sets us apart is our commitment to delivering these services with simplicity, transparency, and a personal touch that distinguishes us from larger FM providers.
    
    PROJECTS & MANAGEMENT
    
    In addition to our maintenance expertise, we excel in project delivery and estate management solutions. Whether it's overseeing minor repairs, executing PPM schedules, or managing extensive estates, count on IEM to handle it with precision and care.
    
    STRAIGHTFORWARD APPROACH
    
    We believe in straightforward communication and transparent processes. At IEM, we're not just service providers; we're proactive partners dedicated to maximising the efficiency and longevity of your facilities.
    
    107 (1)
    SECTORS
    With extensive industry experience, IEM efficiently handles a wide array of facilities tasks. From healthcare to education and retail, our expertise ensures seamless management of your facilities management program.
    Iem Sectors
    SERVICES
    Disciplines - Planned & Reactive
    Artboard 1
    Electrical & Mechanical
    Artboard 2
    Refrigeration
    Artboard 3
    Asbestos Management and Removal
    Artboard 4
    Plumbing Waste and Drainage
    Artboard 5
    Lighting LED Roll-outs & Design
    Artboard 6
    Civils
    Artboard 7
    Fire Systems & Risk Assessments
    Artboard 8
    Roofing
    Artboard 9
    Water Risk Assessments and Legionella
    Artboard 10
    Fit outs and Construction
    Artboard 11
    HVAC (Heating, Ventilation & Air-Conditioning)
    Artboard 12
    Intruder Systems and CCTV
    Artboard 13
    LEPC (Lifts, Escalators & Passenger Conveyors)
    Artboard 14
    Roller Shutter & Automatic Doors
    Artboard 15
    Utilities Connections (Gas, Electric, Water)
    Services Map
    Support Services
    Artboard 16
    Health and Safety Management
    Artboard 17
    CDM
    Artboard 18
    Listed Buildings & Conservation Area
    Artboard 19
    Principal Designers
    Artboard 20
    Main Contractor
    Artboard 21
    Tender Production & Support
    Artboard 22
    Dilapidation Support & Assessments
    Artboard 23
    ESOS
    Artboard 24

  
   1.Extra Information.
    Category Name Entered:  Best Company To Work For\n\u2022\tName of Entrant: Christy Smith\n\u2022\tEmail Address of Entrant: 
    c.smith@integrated-em.com\n\u2022\tDirect Telephone Number of Entrant:  07944624543\n\u2022\tName of Entry: Integrated Estate Management Ltd 
    (IEM) \nWho are IEM? We are a forward-thinking FM company that specialises in hard services across the UK, utilising a robust network of 
    Partners to deliver comprehensive solutions. We support many key clients, ranging from providing reactive maintenance to full FM coverage 
    and managing large-scale projects. Our mission is simple: simplifying the complexity of Facilities Management for our clients. Too often, 
    FM managers sit at the back during Christmas parties, only noticed when a chair or table breaks, and given the blame! We want to change this 
    #narrative by ensuring that the FM teams we work with receive the recognition they deserve. Our goal is for these managers to be seen as 
    integral to the success of their organisations.

    At IEM, our story began with a vision born out of adversity. The initial few of us joined IEM after being made redundant during the challenging times of COVID-19. Our lives were turned upside down, but this difficult situation inspired Alistair to create something different. He founded IEM with a clear goal: not to be the most profitable company in the world, but to be a company that genuinely cares about its people and clients.\nFrom the beginning, our focus has been on building a lean team that is treated fairly, empowered, and supported every step of the way. Our approach has been to remove any sense of hierarchy; it's not just the Directors and Managers who matter here\u2014everyone plays a crucial role. This is central to our culture and defines who we are as a company.
    Our Values: At IEM, our core values drive everything we do and shape the environment we create for both our team and our clients. We are skilful and ambitious, always striving for excellence in our work and seeking opportunities to grow and improve. We genuinely care about our people, our clients, and the communities we serve. With a positive mindset, we embrace challenges as opportunities, focusing on solutions and fostering a culture of optimism and teamwork. We are agile and brave, adapting quickly to change and confidently taking on new challenges in an ever-evolving industry. We own it and deliver, taking responsibility for our actions and outcomes, always holding ourselves to the highest standards. Most importantly, we do this together collaborating, supporting one another, and creating an environment where every individual feels empowered to contribute.\nThese values are more than just words; they are the foundation of who we are and how we work.
    
    Key Initiatives and Employee Benefits:\n1.\tCompany-Wide Bonus: At IEM, we share our success with our people. Last year, after hitting our turnover target, we awarded every employee with a company-wide bonus. Those with a full year of service took home a minimum of \u00a36,000, with pro-rated bonuses for others. This initiative saw 75% of our annual profit given to our team, a reflection of our belief that success should be shared. We are continuing with a similar bonus structure this year, and it\u2019s something we are incredibly excited about. This financial recognition reflects our commitment to rewarding the entire team for their hard work. \n2.\tPrivate Healthcare: We provide comprehensive private healthcare to all employees who pass their probation. This isn't just basic healthcare; we've upgraded the package to include mental health care support, dental coverage, and eye care. We believe in supporting the complete well-being of our staff\u2014physically, mentally, and emotionally. By offering enhanced healthcare benefits, we ensure our employees feel supported both at work and in their personal lives. Mental health care is especially crucial, and we want our team to have access to the resources they need to stay healthy and thrive.\n3.\tEmployee-Led Initiatives: We listen to our people. For example, after requests from our team, we are implementing \"bring your dog to work\" days, a simple but meaningful change that boosts morale and makes the workplace more enjoyable. These days not only add a sense of fun to the work environment but also contribute to reducing stress and improving mental well-being. Studies have shown that interacting with pets can lower anxiety and increase positivity, making this initiative a valuable addition to our workplace. \n4.\tPromotion from Within & Growth Opportunities: As we've grown from a team of 3-4 people to over 30, we\u2019re committed to succession planning. Whether someone wants to become a project manager or chase a completely different career path, such as becoming an astronaut, we\u2019re here to help them on their journey. \n5.\tProfessional Development: We are committed to investing in the growth and development of our team. Currently, four of our staff members are receiving coaching to help them achieve their individual goals. We offer a wide range of training opportunities tailored to each team member's ambitions, ensuring everyone has the tools they need to grow in their roles. This includes carrying out a company-wide skills matrix, which will allow us to offer IWFM memberships and better understand everyone\u2019s knowledge and development needs. Just this week, our team participated in a \"Delivering Excellent Service Consistently\" training session, and we have several staff members undergone first aid training. Additionally, we provide full access to the IHASCO training platform, where all employees can benefit from a wide variety of modules. \n6.\tPersonalised Support: At IEM, we go above and beyond to support our people in times of need. Recently, when one of our team members' car broke down, we ensured they had a courtesy car ready so they weren\u2019t stuck at home. This small act reflects our broader ethos\u2014our employees' personal challenges are our challenges, and we\u2019ll always step up to help.\n7.\tReward and Recognition: At IEM, we believe in celebrating the achievements and milestones of our team. We ensure that every work anniversary is marked with a thoughtful reward. For example, I recently received a bracelet for my 4-year anniversary, which was extra special because the team remembered I had my eye on it. A few years ago, during a challenging period, I was gifted a Chanel handbag, a gesture (and handbag) that I\u2019ll cherish forever! We also encourage the team to run their own initiatives\u2014right now, we\u2019re doing a \"Star of the Week\" for reducing open tasks, which has been a big hit, keeping everyone motivated and engaged.\n8.\tAdditional Benefits: we offer a range of thoughtful benefits that reflect our commitment to creating a supportive work environment. This includes birthdays off, an additional annual leave day for each year of service (uncapped), and flexibility to manage work-life balance. We understand that life happens outside of work, so we allow our team the flexibility to work from home when needed or adjust schedules around childcare commitments. Recently, a new starter was struggling with \"single dad guilt\" due to childcare issues during school holidays, so we gave him every Friday off, fully paid, for the first five weeks of his employment to support him during that transition. \nClient Care and Dedication: Our dedication to clients mirrors our care for employees. A standout example of this commitment occurred when one of our clients needed urgent furniture removal at a site five hours away from our helpdesk. Despite being unable to secure a team in time, one of our helpdesk team members, who was fully qualified to carry out the removal, took it upon themselves to hire a van and drive to the site personally to complete the task. This willingness to go the extra mile is ingrained in our culture and exemplifies how we consistently prioritise our clients\u2019 needs, ensuring they receive top-tier service.
    
    Team Spirit and Collaboration: One of our strongest assets is the close-knit, collaborative environment we\u2019ve cultivated. Despite our growth, we maintain the spirit of a small, tightly connected team. Regular social events, team-building activities, and an inclusive culture make IEM a fun and dynamic place to work. Recently, we enjoyed an exhilarating team-building day at a rage room and axe throwing event, which was a huge hit with the team. We also host fantastic Christmas parties every year and an annual BBQ that everyone looks forward to. This sense of togetherness fuels our productivity and makes IEM an exciting and supportive workplace.
    
    Mental Health and Wellbeing Support: We understand the importance of mental health, especially in today\u2019s high-pressure world. In addition to healthcare benefits and counselling available, we are rolling out more mental health support initiatives to ensure that everyone at IEM feels cared for, both physically and mentally, which our Mental health champion is involved in.
    
    Charity: At IEM, we are proud to support Scotty's Little Soldiers, a charity dedicated to aiding children who have lost parents serving in the military or veterans who have passed away. Supporting such a meaningful cause aligns with our core values of care, empathy, and giving back. It\u2019s not just about being successful in business for us; it\u2019s also about making a difference in the wider community and positively impacting the lives of those in need. Our team is deeply committed to this cause, and we continually look for ways to support and give back.
    Veterans Support: Our founder, Alistair, is an ex-armed forces member and co-chair of the IWFM Veterans in FM network, which underscores our commitment to supporting veterans transitioning into civilian employment. At IEM, we proudly hold the Armed Forces Covenant Bronze Award and are actively working towards achieving the Silver Award. We are dedicated to creating pathways for veterans to build successful careers in FM, providing tailored support, mentorship, and opportunities to leverage the valuable skills they bring from their military service. Supporting veterans isn\u2019t just a pledge\u2014it\u2019s an integral part of our company\u2019s values and mission.
    
    Accreditations and Awards: We are proud recipients of the Silver Award for Neutral Carbon Zone, which underscores our dedication to reducing our environmental impact and supporting a sustainable future. Our ISO certifications (9001, 14001, 45001) demonstrate our adherence to best practices in quality management, environmental stewardship, and occupational health and safety. We are also accredited by Safe Contractor, highlighting our commitment to maintaining high standards of health and safety across all operations. Our founder, Alistair, has been recognised as one of the Top 50 Workplace Leaders, a prestigious honour that showcases his leadership and commitment to fostering a positive workplace culture. In addition, IEM holds the National Living Wage accreditation, ensuring that all our employees are compensated fairly, in line with the real cost of living. These achievements exemplify our dedication to industry standards, employee well-being, and environmental responsibility.
    
    Diversity and inclusion: We recognise that diversity and inclusion are essential to creating a vibrant and innovative workplace. We actively promote awareness of these values through our dedicated Diversity Champion, who helps to normalise conversations around equality and representation.\nMoving forward, we will establish a committee focused on diversity and inclusion, which will introduce new awareness days and initiatives aimed at fostering a more inclusive environment. Our commitment to becoming a Disability Confident Employer reflects our desire to nurture a culture where everyone feels comfortable being themselves. We are dedicated to promoting a supportive atmosphere that celebrates equality and diversity, ensuring that all team members are valued and empowered to contribute their unique perspectives.
    Employee Turnover \u2013 What Employee Turnover?! Since our inception, IEM has proudly maintained an exceptional employee retention rate, having lost only one permanent member of staff. This remarkable achievement speaks volumes about our company culture, values, and the supportive environment we've cultivated.

   The Next 12 Months at IEM The upcoming year promises exciting developments at IEM as we continue to invest in our people and business. We are introducing death in service benefits to provide added peace of mind to our team and their families. To ensure transparency and fairness, we will be rolling out a pay banding, offering clear career progression and salary structures. We're also committed to enhancing our benefits with better pensions to support long-term financial well-being.\nSabbaticals are on the horizon to offer our staff time to pursue personal passions or recharge, ensuring they come back more motivated and fulfilled. We're also setting our sights on B Corp certification, which will be a huge deal for us!\nTeam spirit will remain a core focus, with exciting team-building activities, such as a company-wide sports day, to foster collaboration and camaraderie. Additionally, we will launch our very own Corporate University, providing ongoing professional development and training opportunities tailored to each employee's growth ambitions.

   Conclusion: At IEM, it\u2019s not just about profits, it\u2019s about people. We believe that a company is only as strong as the people behind it, and that\u2019s why we strive to create a work environment where every employee feels valued, supported, and empowered. From company-wide bonuses and private healthcare to flexible working arrangements and personalised support, we\u2019re always looking for ways to make IEM the best company to work for.\nWe hope this application demonstrates our unwavering commitment to our employees, clients, and community\u2014and why we believe IEM truly deserves to be recognised as the Best Company to Work For.
   Alistair Scott | Operations Director\nIntegrated Estate Management Ltd\n07827 914166\nAll terms and agreements outlined within the\ncompliant bid document are by agreement of the\ncompliant bid proposal agreed to, against the\nadditional tasks outlined within this document.\nI trust this document has provided a brief overview\nof IEM and goes a little toward our passion to\nsimplify the complexity of building management.\nIf there are any questions or clarifications, please do\nnot hesitate to contact us.\nKind regards,


  REQUEST FOR INFORMATION \u2013 MEBF Maintenance for Osborne Clarke LLP\nMEBF Tender \u2013 Hard Services Provision for Osborne Clarke (OC), RFI issued by IM&SS Ltd.\nSite Addresses\nLondon \u2013 One London Wall, Barbican, London, EC2Y 5EB\nBristol \u2013 Halo, Counter slip, Bristol, BS1 6AJ\nReading \u2013 3, 23 The Forbury, Forbury Road, Reading, RG1 3JH\nDate of Issue: 8th November 2023\nContractors RFI Submission Deadline: 17.00 \u2013 Friday 17th November 2023\nSubmission by email to: - keith.parker@imassltd.com\nAbout\nOsborne Clarke LLP is an international legal practice headquartered in London, England with offices in the United Kingdom, Germany, Italy, Belgium, Spain, Sweden, France, the Netherlands, China, Hong Kong, India, Singapore, and the United States. The firm has over 270 partners and 1,600 employees spread across its 26 offices around the world.\nOutline Contract Scope\nWithin the contract scope, the selected service provider will be entrusted with delivering a range of hard FM services. Broadly outlined as the following: -\nM&E\n\u2022\nPlanned & reactive maintenance of the mechanical & electrical services.\n\u2022\nPlanned and reactive maintenance of domestic water and drainage systems\n\u2022\nPlanned and reactive maintenance to life safety systems\n\u2022\nPortable appliance testing\n\u2022\nAsset validation and condition reporting\n\u2022\nProvision and management of the CAFM platform\n\u2022\nManagement of specialist subcontractors\n\u2022\nAsset Life cycle analysis and management\n\u2022\nEnergy monitoring and management\n\u2022\nEnvironmental management\n\u2022\nLegislation compliance\nBuilding Fabric\n\u2022\nRepair and maintenance of internal structures \u2013 walls, ceilings etc\n\u2022\nRepair and maintenance to internal flooring and coverings\n\u2022\nRepair and maintenance to internal doors, blinds and windows\n\u2022\nRepair and maintenance of fire doors and passive fire stopping.\nThe successful service provider will be expected to submit monthly reports to transparently outline their service performance against the contractual SLA\u2019s and KPI\u2019s. Effective and regular communication, as well as coordination with the client's designated point of contact, are deemed as being pivotal aspects of this service provision. Furthermore, OC LLP encourage service providers to proactively suggest and adopt environmentally friendly practices as part of the service delivery and will be a key focus point as the new contract progresses.\nGuidance notes for the completion of the RFI\nThe purpose of this RFI is to provide Osborne Clarke LLP with sufficient information about potential Suppliers to allow an assessment to be made of their capability and suitability to be included into a shortlist who will be invited to tender for the contract.\nYou must answer all questions fully.\nAll questions should be answered in English. The questions require concise, honest, and factual responses. Please note where a maximum word limit applies to a section of the form, please adhere to this limit.\nWhere you need to draw attention to a separate document included as part of your response to answer a question, please ensure you provide clarity of which document, which page, and which paragraph/sentence you are drawing attention to.\nEach question must be answered in full using the same section and numbering format as appears in the RFI.\nShould you have any queries regarding this RFI or require any assistance please submit your question by e-mailing the following address:\nkeith.parker@imassltd.com\nEvaluation Criteria RFI Evaluation (Questions Answered Fully) Evaluation Criteria Pass/Fail A - Company Information Pass/Fail B - Financial Information Pass/Fail C - Insurance Pass/Fail (Scored) D - Technical Capacity and Resource Pass/Fail (Scored) E - Quality and Standards Pass/Fail (Scored) F - Health and Safety Pass/Fail (Scored) G - Equality and Diversity Pass/Fail H - Declaration\nOC LLP intends to shortlist 3 highest ranked Suppliers to be selected for Invitation to Tender (RFP).\nSECTION A: COMPANY INFORMATION & STRUCTURE\nA1. Name of Company/organisation making application.\nIntegrated Estate Management Ltd A2. Trading name if different from above.\nIEM A3. Key contact details (within the Supplier). Please note that this will be the address and person all correspondence will be addressed to regarding this RFI and resultant RFP if successful to be shortlisted. Name:\nAlistair Scott Position within organisation:\nFounder Address:\nWeston Business Centre\nHawkins Road\nColchester\nEssex\nCO2 8JX Telephone:\n020 3772 4188 Mobile Phone:\n07827914166 E-mail:\nAlistair.scott@integrated-em.com Web Site:\nhttps://integrated-em.com\nA4. Registered office (if different from above).\nOffice 5, Boleyn Suite,\nHever Road,\nEdenbridge\nKent,\nTN8 7NP\nA5. Are you or is your organisation a: Sole Trader?\nPartnership?\nPrivate Limited Company?\nYes Public limited Company?\nRegistered Charity?\nOther?\nPlease Specify?\nA6. Limited Companies Please state the companies date of incorporation and registration number under the Companies Act 1985. OR\nDate\n02/11/2018\nRegistration Number\n11657337\nDate of registration and the company's registration number under the Industrial and Provident Societies Acts 1965 to 1978. OR\nDate\nNumber\nPartnerships Please state the date the partnership was formed, began trading and Total number of partners. Are the partnerships being a member of a group? If \u201cYes,\u201d detail other relationships within the group and comment on the group structure. OR\nDate\nNumber\nTotal Number of Partners\nAdditional Comments\nSole Trader\nDate\nDate when Supplier began trading\nA7. If the Supplier is a member of a group of companies or subsidiary of another company as defined by Section 736 (1) of the Companies Act 1985, give the names and company numbers of the holding company and any companies in-between you and the holding company, clearly stating the relationship with your organisation.\nCompany Name\nCompany Number\nRelationship\nN/A\nA8. Is the parent company or ultimate holding company prepared to guarantee the performance of the Supplier?\nYes:\nNo:\nN/A\nIf yes, please provide: Name of Company\nRegistration number\nRelationship with your company\nA9. What is your organisation\u2019s VAT number?\n310404272\nSECTION B: FINANCIAL INFORMATION & REFERENCE INFORMATION\nB1 Name of Bankers:\nSantander Address of Bankers:\n2 Triton Square,\nRegents Place\nLondon,\nNW1 3AN Name of Auditors:\nN/A\nB2. Please provide details of the past three years turnover of the company Year Ending 2019 - 20\n\u00a3122,000\nYear Ending 2020 - 21\n\u00a3681,000\nYear Ending 2021 - 22\n\u00a31,174,000\nB3. Please provide details of three existing customers with similar contracts that we can contact for references.\nRef 1 - Company name, contact details, contract value\nChatham House\nLisa O\u2019Daly \u2013 Managing Director\nlodaly@chathamhouse.org\n\u00a3560,000\nRef 2 - Company name, contact details, contract value\nThe Knightsbridge\nChris Barrass \u2013 Managing Director\nchris.barrass@theknightsbridge.com\n\u00a31,100,000 Ref 3 - Company name, contact details, contract value\nSean Donnelly\nHead of Procurement\nIVC\nsean.donnelly@ivcevidensia.com\n\u00a37,000,000\nSECTION C: INSURANCE\nPlease provide details of all insurance cover currently in force. If you reach and are successful at the tender stage, adequate insurance cover will be required. C1. Please insert copy documents of your organisation\u2019s insurance cover in respect of employer\u2019s liability, public liability, and any other relevant policies (including details of Fidelity & PI cover). Please summarise these below. Policy Insurer Indemnity Limit (\u00a3)\nPublic and Products Liability\nGallagher\n\u00a310,000,000\nEmployers Liability\nGallagher\n\u00a310,000,000\nProfessional Indemnity\nGallagher\n\u00a32,000,000\nSECTION D: TECHNICAL CAPACITY AND RESOURCES\nD1. Please list your Top 3 Clients by Contract Value for similar contracts that your organisation has carried out within the last 3 years.\nClients Name\nScope of the Services\nTotal Value of the Contract\nContract Duration\nIVC\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a37,000,000\n3+2years\nStonegate\nProjects and Reactive Support\n\u00a32,000,000\n2 years\nThe Knightsbridge\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a31,100,000\n3+2 years\nD2. Please list your Employees Structure & Nos. for that your organisation has employed for each of the last 3 years. Category 2023 2022 2021 Managers / Supervisors\n5\n2\n2 Operatives\n7\n2\n1 Apprentices\n1\n1\n0 Administrative Staff\n2\n1\n1\nD3. Please describe your organisation\u2019s approach to initial staff training in relation to the buildings they will be maintaining on this contract (1000 words max)\nAll our supply chain partners are fully inducted and trained before they can be on-boarded with IEM.\nWe have a thorough partner on-boarding process that we are happy to share if required, as a high-level overview:\n\u2022\nIEM has a dedicated Supply Chain Manager who ensures all our partners are fully onboarded, have gone through the IEM induction process then trained.\n\u2022\nA PQQ is always carried out, then we will meet with all new partners.\n\u2022\nDuring the induction process we ensure our partners are aware of our culture, values and service levels, as well as SLA\u2019s and individual customer expectations (as SLA\u2019s and prioritisation levels can vary from client-to-client)\n\u2022\nAll our partners must also be safe contractor trained and accredited before they are able to work with any of our customers.\n\u2022\nAfter initial on-boarding we also have a sign off period, this process is carried out by our Operations Manager, Technical Manager and Supply Chain Manager\n\u2022\nAll partners have to be trained in our AIMS system.\n\u2022\nAll insurance and certifications are checked, these have to be correct and live for contractors to be able to work with IEM, our AIMS system will send us reminders as to when these are due to expire so that we can monitor.\n\u2022\nFull Health & Safety checks are carried out.\n\u2022\nRegular Performance reviews are scheduled from the outset.\nAlong with partner onboarding internal staff go through a thorough induction, which focuses on IEM ethos, system training (with trade tests throughout the initial 3 weeks process and further scheduled throughout the year), and customer service training.\nWe are happy to share the internal induction precis if required.\nD3.1 Please describe your organisation\u2019s approach to the control and management of specialist sub-contractors (1000 words max).\nSome of the information is covered above, however, some of the main points are as follows:\n\u2022\nWe have a dedicated supply chain manager that manages all our sub-contractors, both in relation to onboarding but then also from a continuous improvement perspective\n\u2022\nWith more than 1500 contractors and sub-contractors that work with us, all hard FM disciplines are covered, so we have to be very diligent in relation to their control and management.\n\u2022\nAt the outset we will have a formalised partnership agreement that is agreed by both IEM and sub-contractor, this includes the non-negotiable of everyone that works with IEM being Alcumus Safe Contractor accredited.\n\u2022\nWe have very clear terms and SLA\u2019s, which we are happy to share, and these are in place when our contractors start having conversations with us.\n\u2022\nAfter on-boarding and an initial probation period is completed, the sub-contractors are signed off and performance reviews are put in place which are then carried out by our supply chain manager.\n\u2022\nPart of our continuous improvement and monitoring process includes regular feedback documents being sent to our customers in relation to all our partners, we then share this during all our performance reviews.\nD4. What mechanisms do you have in place to ensure that you maintain high standards for the provision of MEBF maintenance within the built environment. (1000 words max).\nWe continually seek continual improvement to ensure our service delivery remains to a high standard, this includes.\n\u2022\nCompliance with Regulations: we ensure strict adherence to statutory compliance and legal compliances using CIBSE Guide M as an example, and safety standards.\n\u2022\nQuality Management Systems (QMS): Implementing and maintaining QMS standards such as ISO 9001 helps establish and follow processes that ensure high-quality service delivery.\n\u2022\nSkilled Workforce: Ensuring that contractor partner's maintenance teams are well-trained, certified, and equipped with the necessary skills and knowledge to perform their duties effectively and safely.\n\u2022\nPreventive Maintenance Programs: Developing and implementing preventive maintenance schedules to address potential issues proactively, thus minimising disruptions and costly repairs.\n\u2022\nAsset Management: Implementing robust asset management systems to monitor the condition of equipment and facilities, plan for replacements or repairs, and maximize the lifespan of assets.\n\u2022\nTechnology Integration: Using advanced technologies, such as CAFAM Systems, to streamline maintenance processes, monitor work orders, and manage resources efficiently.\n\u2022\nContinuous Improvement: Establishing a culture of continuous improvement by regularly reviewing and updating processes based on feedback from clients and staff to enhance efficiency and effectiveness.\n\u2022\nEmergency Response Planning: Developing and regularly updating emergency response plans to handle unforeseen events or crises effectively, minimizing potential damage and downtime.\n\u2022\nSupplier and Contractor Management: Selecting reliable suppliers and contractors, setting clear expectations and performance criteria, and regularly assessing their performance.\n\u2022\nPerformance Metrics: Defining and measuring key performance indicators (KPIs) to assess the effectiveness of maintenance activities and identify areas for improvement.\n\u2022\nEnvironmental Sustainability: Integrating environmentally sustainable practices into maintenance activities to minimize the impact on the environment and promote long-term sustainability.\n\u2022\nClient Communication: Maintaining open and transparent communication with clients regarding maintenance activities, schedules, and any potential disruptions.\n\u2022\nTraining and Development: Providing ongoing training and development opportunities for staff to keep them updated on industry best practices and new technologies.\n\u2022\nRegular Audits and Inspections: Conducting regular audits and inspections to ensure that maintenance activities align with established standards and procedures.\n\u2022\nFeedback Mechanisms: Establishing mechanisms for collecting feedback from clients and stakeholders to continuously assess and improve service quality.\nD5. Please provide a summary of your procedures for contract Management and Quality Audit (1000 words max).\nIEM are fully Safe Contractor as well as Principal Safety Accredited, this includes annual audits on our processes, with Safe Contractor carrying out monthly automated assessments on areas such as insurances, H&S, financial and sustainability.\nWe use the Safe Contractor portal to carry out the base management of our supply chain partners.\nWe also carry out our quarterly assessment meeting with our supply chain partners, which covers the data gathered during task visits, cost management and response management, the spot site visit audits are also evaluated at these meetings.\nWe also have our internal annual ISO 9001, 14001 and 45001 audits.\nD6. Can you provide an example of how you have ensured that you provide an exceptional service to a customer with buildings in multiple locations. (500 words max).\nAlmost all our clients, apart from the highly prestigious Chatham House and Knightsbridge apartments are multi-site locations.\nSupporting multi-site locations is IEM\u2019s sweet spot. The quantity of contractors that we have, with the nationwide geographical spread, means we offer support across the whole of the UK.\nOur clients include IVC vets (1400 sites), Stonegate Pubs (4500 sites) Arnold Clark (250 sites) these are just a few examples.\nAs mentioned, we have full nationwide coverage (Inc Ireland) and within almost all geographical locations, we operate 3 tiers of contractors per discipline, this gives IEM more choices and supports us from an availability and pricing perspective.\nAt the initial on-boarding, our operational processes and rhythms are agreed, these are then carried out during the relationship.\nAs an example, one of our partners, that works with IEM on IVC fire and security disciplines, have the following ways of working (Others are very similar):\n\u2022\nA Monday Operational Call to go through all outstanding jobs.\n\u2022\nA deep dive into SLA\u2019s and delivery weekly\n\u2022\nA monthly more in-depth dive call\n\u2022\nA visit to partners site every quarter to go through the account in detail and discuss what is working and areas of improvement.\nD7. Please provide an overview of your company\u2019s approach to corporate social responsibility (CSR)? Please provide a list of six core operational aspects that your CSR policy considers. (1000 words max).\nIEM truly values itself in relation to corporate social responsibility and it is a key part of what makes us what we are, a few examples of these are below and these can be discussed if application is progressed:\n\u2022\nWe are NCZ accredited (Neutral Carbon Zone) This accreditation provides us with independent verification and is an internationally recognised accreditation showing that IEM is following the right processes and procedures to get us to net zero. This is renewed yearly. We are also now working to ensure a key part of our supply chain is also accredited.\n\u2022\nOur vision, mission and objectives were created by the whole team, is kept alive through various channels and before any new staff members can work with us, they must have done our induction which includes all of the above. This ensures alignment and continuity\n\u2022\nOur goals and objectives are created yearly with the full team\u2019s involvements, this includes setting objectives for the year ahead and reviewing previous years performance. What differentiates IEM, is that annual goal setting is completed at a full team meeting of all employees not just senior management.\n\u2022\nWe are very strong exponents of supporting the veteran military community through a variety of means.\no\nAmbassadors and prime sponsors of one of the UK\u2019s leading military charities Care After Combat\no\nFounder Alistair Scott is Director of IWFM audit and risk committee and jointly formed the IWFM \u201cVeteran\u2019s in FM\u201d Professional Networking Group..\n\u2022\nIEM are proud to be National Living Wage Accredited.\n\u2022\nWe and every one of our contractors are Safe Contractor accredited.\nSECTION E: QUALITY AND STANDARDS\nE1. Please insert details (list) of the quality assurance certification that your company holds e.g., BS EN ISO9001, ISO14001, CHAS, IIP or equivalents. Please provide copies of certificates in a separate file.
  \n\u2022\nISO9001\n\u2022\nISO14001\n\u2022\nISO45001\n\u2022\nSafe Contractor\n\u2022\nPrincipal Safety\nE2. Please provide details of any memberships of trade associations and other relevant accreditations. Please provide copies of certificates in a separate file.\n\u2022\nBESA Associate\n\u2022\nIWFM\n\u2022\nIET\nSECTION F: HEALTH AND SAFETY\nMandatory to be selected to Invitation to Tender. Yes No F1.1 The Supplier must have a written Health and Safety at Work policy? Please note that this document must not be more than 12-months-old.\nYes\nF1.2 Please provide brief details how your Health & Safety Policy is communicated to your staff and the systems and procedures you have in place for monitoring, reviewing, and reporting of Health and Safety issues. (1000 words max).\nThis is covered in depth during our various ISO accreditation process, but a few of the key points are as followed:\n\u2022\nWe have a separate Health and Safety committee, represented by a variety of team members not just senior management.\n\u2022\nAll minutes and actions are documented, with clear next steps.\n\u2022\nThis meeting is held monthly and an external H+S representative attends and is also accountable for training.\n\u2022\nH+S is a key part of our induction process.\n\u2022\nAll minutes and next steps are always on out staff communication board.\n\u2022\nAny Health and Safety issues are reported through the H+S internal and external rep, these are actioned and recorded, they are also covered at our H+S meeting as well as our normal monthly meeting.\nF1.3 H&S Policy Attached:\nYes\nF1.4 Does your organisation have any Health & Safety Accreditation, e.g., ISO 18001 or equivalent?\nSafe Contractor\nPrincipal Safety\nISO:9001\nF1.5 If \u201cYes,\u201d please provide copies of any relevant certificates as separate attachments\nF3. Please detail any HSE / local authority enforcing action taken against your company in the last three\nyears (up to 500 words per incident):\nN/A\nF4. Please include details any RIDDOR reportable accidents by your company within the last three years.\nN/A\nSECTION G. EQUALITY & DIVERSITY\nYour company will be evaluated for equality and diversity in employment based on your answers to these questions. Please ensure that you answer them all.\nPlease provide sufficient information to enable OC to make a fair and accurate assessment of how, as an employer and/or service provider, you have dealt with equality issues.\nMandatory to be selected to Invitation to Tender. Yes No G1. The Supplier must have a written Equalities & Diversity Policy? Please note that this document must not be more than 12 months old.\nYES\nG2. Equalities & Diversity Policy Attached:\nG3. Is it your Company policy as an employer to comply with your statutory obligations under the Equality Act 2010 (or European equivalents), and accordingly your practice not to treat one group less favourably than others?\nYES\nG4. Please provide details of the Right to Work in UK \u2013 Visa Checks you operate? (1000 words max).\nThe Right to work is assessed during the interview stage, the preferred process is to check the applicant's right to work using the online portal (this requires the applicant to share their code).\nIf this isn\u2019t possible, we use our employment partner who assesses the right to work using the applicant's documents and Identity Document Validation Technology (IDVT).\nSECTION H: DECLARATION\nH1: Declaration Name, Position & Signature Date We confirm and declare that the contents of this RFI submission and all details stated above are true and correct.\nAlistair Scott\nFounder\n16th Nov 2023\n3. Technical Resources\n3.1 Company Background\nIEM is honoured to submit our tender for your Hard FM Services at Voyager Care, marking the beginning of a partnership aimed at revolutionising facilities management standards. At IEM, we are driven by a singular mission: to simplify the complexities of estate management while delivering unparalleled expertise, innovative solutions, and unwavering excellence.\nWith over 25 years of experience in facilities management, IEM is not just another service provider\u2014we\u2019re your strategic partners in building efficient and thriving estates. Based in Colchester, our team of professionals prioritises your business needs, offering tailored solutions and expert advice whenever required. Supported by an extensive network of 2,000 skilled engineers ensures that we can swiftly address challenges across diverse geographical locations, extending our support far beyond regional boundaries.\nAt the core of IEM\u2019s approach lies a comprehensive Five Point Plan, meticulously crafted to refine operational workflow and boost efficiency. This plan encompasses a deep understanding of assets, insight into their condition, adherence to compliance standards, clarity in prioritising objectives, and excellence in delivery management. Through strategic planning and continuous improvement efforts, we ensure that every goal is met with precision and effectiveness.\nOur commitment to Voyage Care goes beyond just providing services; it\u2019s about fostering collaboration, open and honest communication, and mutual trust. Like Voyage Care, we champion a people centric approach, collaboration, trust, exceptional outcomes, and equity for everyone. This alignment forms the foundations of our partnership, ensuring that our collaboration yields meaningful results.\nAs part of our service model, we employ dedicated personnel who specialise in your estate\u2019s specific operational needs and preferences. This tailored approach, combined with continuous training and robust feedback mechanisms, guarantees personalised and adaptable customer care.\nMoreover, our dedication to corporate social responsibility extends into the communities where Voyage Care operates. Through initiatives such as volunteer programs, charitable donations, and sponsorships, we support vital causes such as Care after Combat and the Armed Forces Covenant, making a positive impact on those who have served our country. As an accredited Real Living Wage employer, we ensure fair compensation for all our staff. Our dedication to corporate social responsibility extends into the communities where Voyage Care operates, with initiatives such as volunteer programs and charitable donations making a positive impact.\nIn conclusion, IEM is fully committed to supporting Voyage Care\u2019s mission by delivering tailored, high-quality services backed by expertise, innovation, and a people first approach. Together, through collaboration, open and honest communication, we can achieve remarkable outcomes and make a meaningful difference in the lives of those we serve.\n3.2 CAFM Experience\nWe proudly embrace cutting-edge technology to elevate the efficiency and effectiveness of our service delivery. Central to our delivery is the integration of the 24-hour help desk and the AiMS CAFM system, which together ensure seamless operations and communication. The around-the-clock availability of our technical help desk guarantees you have immediate support and assistance, day or night. This unwavering support is instrumental in maintaining operational continuity and reducing any disruptions to daily activities, providing peace of mind and reliability.\nFurthermore, the AiMS CAFM system stands as a pillar of our technological strategy, offering real-time data on asset performance, maintenance schedules, compliance statuses, and more. This system not only streamlines facility management processes but also enhances\n\u201cStrategic partners in building efficient and\nthriving estates.\u201d\n6\ndecision-making and resource allocation. With the ability to monitor work orders, manage maintenance tasks, and ensure service delivery transparency in real-time, we set a new standard for accountability and efficiency in contract delivery.\n3.3 Account Structure\nIEM\u2019s mobilisation team will engage closely with Voyage Care to meticulously prepare for a flawless launch and integration. We understand the significant impact of maintaining consistency and offer the assurance of having an experienced and knowledgeable team in place throughout all pivotal phases, including the transition to business as usual.\nTo facilitate a smooth implementation and migration, our Operations Manager, Implementation Specialists, Technical Services Manager and Client Account Manager will be integral, providing steadfast support and expertise. This team will not only be a constant during the mobilisation phase but will also ensure stability and continuity as we shift into regular operations.\nIEM is committed to your success beyond the initial phase, offering a detailed service review 100 days post-implementation. This critical assessment will evaluate service performance, responsiveness to the dynamic needs of the facility, and the effectiveness of integration into everyday operations. We will identify opportunities for improvements and refinements, ensuring the services we provide are perfectly attuned to Voyage Care\u2019s strategic objectives and are delivered seamlessly as part of our ongoing partnership.\n3.4 Back Office Support\nOur back-office support encompasses a wide range of functions essential for delivering exceptional service to Voyager Care. This includes expertise in HR, Supplier Management, Quality, Health, Safety, and Environment (QHSE), as well as optional services like Energy Management and Asset Management. These functions collectively ensure that our operations are optimised, compliant, and aligned with industry best practices. Our HR team ensures that our staff are well-trained and motivated, while Supplier Management ensures strong relationships with external partners. Quality, Health, Safety, and Environment (QHSE) protocols are rigorously enforced by our dedicated team to mitigate risks and ensure compliance.\nOptional services like Energy Management can optimise energy usage and efficiency, while Asset Management ensures proper maintenance and management of equipment. Together, these functions form the backbone of our operations, enabling us to deliver a high standard of service to Voyager Care.\n3.5 Key Management Personnel\nJoe Benitez\nOur Managing Director Joe, has been an integral part of our company since its inception, overseeing all aspects of the business with a strong focus on Continuous Improvement principles and Operational Efficiency. With a background spanning 25 years in Retail, Joe has held national roles with renowned companies such as Staples, Homebase, IKEA, and Curry\u2019s, among others. His final retail position was as Group Commercial Director for the Dixons Carphone Group, where he spearheaded initiatives to enhance the product and services customer journey, prioritising customer centricity in operational processes. Prior to joining IEM, Joe served as the Group Business Development Director for CloudFM, where he played a pivotal role in driving innovation, earning the company the distinction of being the first FM company to win the Queens Award for Innovation.\nChristy Smith\nChristy, our Operations Manager oversees diverse departments including Help desk, Supply Chain, and Quotations. With over ten years in Facilities Management (FM), she started as a Help desk professional, advancing steadily. Her experience includes notable clients such as Pizza Express, Poundland, and IVC. Holding a Level 4 certificate from IWFM and an ILM Level 3 Diploma in Facilities & Management, Christy continuously enhances her expertise. During her tenure at IEM, she contributed to its growth, evolving from a single department to specialist teams. Previously, as a Senior Account Manager, she honed skills in client management and strategic planning, with roles at CloudFM providing insights into operational excellence and leadership.\n7\nJamie Franklin\nA versatile professional with a unique blend of animation and facilities management expertise. Graduating with an Animation Degree in 2014, Jamie embarked on a career journey that initially delved into retail management through a graduate program at BHS. However, driven by a passion for technical innovation, Jamie transitioned into facilities management in 2017, concurrently undertaking an electromechanical qualification. Joining a prestigious high-end residential business, Jamie quickly ascended the ranks, leveraging management skills to oversee compliance processes and develop a keen passion for energy conservation. Serving as Technical Services Manager at IEM since June 2023, Jamie leads the compliance department, ensuring regulatory adherence while spearheading technical projects with clients. Jamie\u2019s expertise extends to energy management, collaborating closely with clients to optimise energy consumption, enhance asset performance, and reduce environmental impact. With a strategic mindset and a commitment to excellence, Jamie Franklin continues to drive innovation and deliver impactful solutions in technical services and facilities management.\nGoda Tamosiuniene\nHailing from Lithuania, brings a wealth of experience in leisure and tourism to her role as Compliance Manager at IEM. Having transitioned into Facilities Management, she has honed her skills in statutory compliance, asset management, and maintenance processes during her tenure at a prestigious high-end residential company. Joining IEM in July 2023, Goda plays a pivotal role in fortifying the company\u2019s compliance proposition. Her dedication to seamless delivery of statutory PPMs and commitment to client satisfaction distinguish her as a trusted leader in facilities management. Leveraging her expertise, she elevates compliance standards and operational efficiencies, driving positive outcomes for IEM\u2019s clients.\nZsuzsanna Banfi\nOur Supply Chain Lead, brings extensive expertise to her role, overseeing partner mobilisation and performance monitoring. With a background in Operations Management and Supply Chain/Procurement, her strategic approach and attention to detail drive significant impact. Holding a Level 2 Customs Practice and Procedure Award from the UK Customs Academy, she ensures compliance in global trade. Additionally, her Level 5 Advanced Diploma in Supply Chain Management streamlines processes and manages risks. Zsuzsanna\u2019s bachelor\u2019s degree in economics, with a specialisation in Tourism and Hotel Management, enhances insights into economic principles.\nCasey Staff\nOne of the Senior Customer Care Representatives at IEM, Casey commenced her journey on the Help desk in September 2022. This marks her introduction to the Facilities Management sector, following previous roles as a Sales Associate and Office Administrator. She holds a bachelor\u2019s in international business from the University of Brighton, supplemented by a year of studying abroad in Turin, Italy, where she acquired a beginner level of proficiency in Italian. Currently, Casey continues to pursue language studies in both Italian and Dutch while exploring IWFM courses to expand her knowledge. With a keen interest in Projects and Marketing, she aspires to pursue a master\u2019s degree in the near future.\nBeatrice Sandor-Sulutiu\nOur Benchmark Analyst, brings a wealth of experience in estimating to our team, promising to greatly enhance our collaboration with valued partners like yourselves, as well as with our clients. With over five years of extensive experience in estimating and a background in project management and human resources, Beatrice is well-equipped to contribute effectively to our operations. She holds a bachelor\u2019s degree in creative writing, showcasing her diverse skill set and adaptability. Beatrice\u2019s professional journey includes roles as an HR Manager for an Amazon Delivery Partner, and positions as an estimator at Mumford and Wood, AGM, and Delta T, where she consistently delivered high-quality work.\n8\n4. Technical Resources\n4.1 Operational Infrastructure and\nExpertise Overview\nInitiating our partnership with Voyage Care, IEM would\nbe fully equipped to deliver exceptional service with a\ndedicated mobilisation team and a robust workforce\nof qualified engineers. During the mobilisation phase,\nwe conduct comprehensive site visits to familiarise\nourselves with Voyage Care\u2019s estate, ensuring a thorough\nunderstanding of your unique needs and environments.\nOur team comprises a diverse range of skilled engineers,\neach holding essential qualifications such as NVQ Level 3\nin Engineering Maintenance, City & Guilds qualifications\nin Electrical and Mechanical Engineering, and Health &\nSafety certifications like IOSH or NEBOSH. This ensures\nthat every engineer serving Voyage Care\u2019s needs is highly\nqualified and specialised in their respective fields.\nWhile we maintain a core team of engineers, we\nalso leverage a strategic subcontracting strategy to\ncomplement our workforce and enhance service delivery.\nOur extensive national presence allows us to tap into a\nvast network of subcontractors, ensuring efficient and\nreliable service across all your facilities.\nTransparency and alignment with Voyage Care are\nparamount in our service delivery approach. We allocate\ndedicated Help desk members to your account, extensively\ntrained to become experts in your specific needs, ensuring\ncontinuity and consistency in service delivery.\nFurthermore, our commitment to quality is reflected\nin our strict quality control protocols, ensuring that\nour services not only meet but exceed Service Level\nAgreements (SLAs) and Key Performance Indicators\n(KPIs).\nRegular monthly engagement with Voyage Care\nstakeholders for feedback enables us to continuously\nrefine our services to align with your evolving needs and\nmaintain a service standard that mirrors Voyage Care\u2019s\nhigh expectations.\nWe ensure transparency and accountability through\ndetailed weekly and monthly management reports\ndelivered through our advanced CAFM system.\nThese reports cover reactive, Planned Preventative\nMaintenance (PPM), and project tasks, providing insights\ninto SLAs, KPIs, and overall performance.\nOur compliance process follows strict industry standards\noutlined in the SFG20 procedures, ensuring timely and\nbest-practice delivery. Thorough risk assessments and\nmethod statements are conducted prior to any work,\nprioritising safety and efficiency.\nIn conclusion, our approach emphasises precision,\nthoroughness, and transparency, setting the standard\nfor excellence in service delivery and compliance\nmanagement within the industry.\n5. Service Delivery\n5.1 Delivery Approach and Geographic\nScope\nAs we embark on our partnership journey with Voyage\nCare, IEM Facilities Management is prepared to deploy\na dedicated mobilisation team from the onset through\nto the 100-day review milestone. Our foundational\nbelief is that an intimate understanding of your unique\nrequirements and environments is pivotal to delivering\nexceptional service. During the mobilisation phase, our\npriority lies in conducting comprehensive site visits to\nfully acquaint ourselves with every aspect of your estate.\nThis immersive process extends beyond mere\nfamiliarisation; it entails absorbing the unique operations\nthat defines Voyage Care, ensuring our Help desk\nteam is not only well-versed in your layout but also\ndeeply attuned to your operations. This thorough initial\nexploration serves as the basis for crafting a bespoke\n\u201cClient Manual,\u201d a living document that evolves to\naccurately reflect the evolving landscape of your estate.\nBeyond mobilisation, we place significant emphasis on\ncontinuous training and communication to keep our team\ninformed of any developments or changes within Voyage\nCare\u2019s operations. This includes regular refresher training\nsessions, knowledge-sharing forums, and ongoing\nGB & I\nCoverage\n9\n\u201cIEM\u2019s Commitment to Excellence from Day One to Beyond: Customised Solutions, Unwavering Quality and Strategic Partnerships\u201d\nfeedback mechanisms to promptly address any potential issues or areas for improvement.\nTo maintain a consistently high standard of service across all communication channels, we assign dedicated Help desk members to the Voyage Care account. Through focused, extensive training, these individuals become experts in your specific needs, ensuring seamless continuity and consistency in service delivery.\nAt IEM, our service approach for Voyage Care is underpinned by our extensive national presence and a strategic subcontracting strategy, ensuring efficient, reliable, and high-quality service delivery across all your facilities. Our ultimate objective is to meet your bespoke needs with excellence at every juncture, setting new benchmarks in facility management. We prioritise transparency and alignment with Voyage Care through regular updates on ongoing projects, outstanding works, and preferences, facilitated by our AIMS CAFM system for real-time service monitoring and management.\nRegarding on-site routine maintenance, our focus remains squarely on you, ensuring smooth, uninterrupted operations during normal business hours. We collaborate closely with you to develop tailored maintenance schedules that align precisely with your requirements. These custom maintenance plans incorporate preventive measures aimed at minimising downtime and extending the lifespan of your equipment and facilities. Our commitment to delivering superior service extends to compliance with industry standards, including the use of CIPSE, SFG 20, and other recognised best practices in our maintenance protocols.\nMonthly engagement with Voyage Care stakeholders for feedback forms a central component of our process, enabling us to continuously refine our services in alignment with your evolving needs and maintaining a service standard that mirrors Voyage Care\u2019s high expectations.\nIn terms of compliance audits and reporting, our standard procedures include reviews of compliance portals, weekly team meetings with predefined agendas, weekly MI reports through the CAFM system, monthly compliance audits, and QHSE audits. Any findings from these audits are promptly shared with you to ensure transparency and accountability.\nAll performance management elements are underpinned by our company-wide integrated management system, certified to various ISO standards including ISO 9001, ISO 14001, and ISO 45001. This ensures a minimum benchmark of best practice across all areas of our service delivery.\n5.2 Communication Protocols and CAFM Utilisation\nIEM is fully committed to delivering outstanding service to Voyage Care, with effective communication and strategic use of the AIMS CAFM system. Our approach ensures streamlined task management and efficient handling of issues from initiation to resolution. We offer comprehensive support through phone, email, and direct engagement via the AIMS CAFM platform.\nIn developing our robust escalation procedures, we work together with you to tailor these processes to your unique needs.
  This bespoke strategy ensures a transparent and accountable method for issue management, highlighting efficiency and clear communication.\nTo uphold a consistent service level, we assign dedicated Help desk members to the your account, who undergo extensive training to specialise in your operations, guaranteeing continuity and consistency in service delivery. Your Account Manager plays a crucial role in contract management and in providing responsive service, facilitated by regular, structured meetings and proactive communication, ensuring a seamless service experience.\nOur methodical approach extends to the management and submission of all completion documentation, ensuring accuracy, compliance, and efficiency. From reviewing documents to integrating compliance certification with the CAFM system, our process guarantees that every piece of documentation adheres to stringent standards.\nThis meticulous attention to detail, alongside our commitment to continuous improvement and regular quality audits, means service delivery to Voyage Care not only meets but surpasses SLAs and KPIs, aligning perfectly with your evolving standards.\nOur communication strategy is intentionally designed to align with your objectives, employing:\nWeekly Calls\nScheduled discussions with Voyage Care representatives to update on progress, address concerns, and align on objectives.\nComprehensive Weekly Reports\nTailored reports offering insights into performance metrics, issue resolution, and actions taken, ensuring you are always informed and in control.\nAIMS CAFM System\nStreamlined documentation management ensuring\n10\ntransparent access to maintenance records, risk\nassessments, and compliance certificates, keeping you\nfully informed.\nCompliance and Quality Assurance\nUtilising AIMS to manage and verify compliance, providing\npeace of mind with comprehensive documentation and\nsecure access to all project-related information.\nTask Priorities\nOur escalation plan is designed to prioritise issues based\non their severity and potential impact on Voyage Care\u2019s\noperations. From life-threatening situations to non-urgent\nrequests, our categorisation ensures a tailored response\nthat aligns with the urgency of each situation.\nPriority 1: Guaranteeing an immediate 4-hour response\nand resolution within the shortest possible time frame.\nSituations with potential safety hazards or impacting\nbusiness operations\nPriority 2: Ensuring an on-site response within 24 hours\nduring business hours.\nPriority 3: Issues that do not impede business operations\nor pose safety risks fall under with attendance guaranteed\nwithin 5 days.\nPriority 4: Non-urgent requests with a commitment to\nrespond within 30 days.\nThrough these strategies, IEM ensures a partnership with\nVoyage Care that is built on trust, transparency, and a\nmutual commitment to excellence.\nExample of client site comms pieces\n5.3 Team Structure\nIEM presents a specialised team for the Voyage\nCare project, meticulously structured to provide\ncomprehensive Facilities Management (FM) services.\nOur team is adeptly led by Joe Benitez, Managing\nDirector, who brings strategic oversight and a wealth\nof FM and retail sector expertise. Joe will oversee the\noverall management and strategic direction of the\ncontract.\nChristy Smith, serving as Operations Manager, is pivotal\nin the management of day-to-day operations. Her\nextensive experience in FM, underpinned by IWFM and\nILM certifications, ensures effective service delivery and\ncoordination across key operational areas, including the\nHelp desk, Supply Chain, and Quotations.\nJamie Franklin, our Technical Services Manager, enhances\nthe team with his deep-rooted electric\u00e5al engineering\nbackground. Since his start in early 2023, he has actively\ncontributed to elevating our technical service provisions,\nwith a focus on compliance and energy management,\nfortifying our commitment to innovation.\nCasey Staff, our Senior Customer Care Representative,\nexcels in client engagement and resolution management.\nHer background in International Business and\ncommitment to ongoing professional development\nare integral to her role in delivering superior customer\nservice.\nGoda Tamosiuniene, the Compliance Manager,\nbrings over a decade of FM experience to the table,\nensuring adherence to all regulatory requirements and\nmaintenance protocols, thereby safeguarding operational\nintegrity.\nZsuzsanna Banfi, leading our Supply Chain efforts,\nmanages partner relations and supply chain efficacy,\ndrawing upon her expertise in Operations Management\nand Procurement to optimize our processes.\nBeatrice Sandor Sulutiu, as Benchmark Analyst, oversees\nthe issuance of quotes, applying her construction\nindustry experience to align with client expectations and\nproject needs accurately.\nOur proposal encapsulates a team of select professionals,\neach chosen for their specific skill set to ensure a holistic\nand bespoke approach to the Voyage Care project. They\nrepresent the core of our broader team of professionals,\nensuring a coordinated effort to achieve project\nobjectives and service.\n11\nIEM 2024 Organisation Chart\n12\n5.4 Innovation and Added Value\nAt IEM, our commitment to delivering exceptional facility management services for Voyage Care is underpinned by a relentless pursuit of innovation and a culture of adding value. We\u2019re not just about meeting expectations; we\u2019re about redefining them through a blend of cutting-edge solutions, transparent operations, and forward-thinking strategies.\nLeveraging Technology for Efficiency:\nThe heart of our operation lies in the use of the AIMS CAFM system. This powerful platform is our command centre, facilitating task management, progress tracking, and seamless communication through phone, email, and directly within AIMS. It\u2019s designed for efficiency, enabling us to respond swiftly to Voyage Care\u2019s needs with real-time updates and detailed tracking of all activities on site.\nTransparent Communication and Informed Decision Making:\nClear and open communication is a cornerstone of our service delivery. Through regular updates, detailed weekly reports, and ongoing briefings, we keep Voyage Care in the loop at every stage. This ensures that you\u2019re always informed, engaged, and in control.\nProactive Maintenance for Operational Excellence:\nOur approach extends beyond fixing problems as they arise. We anticipate them, using predictive analytics and preventive maintenance to identify and address potential issues before they impact operations. This not only ensures smoother day-to-day operations but also contributes to cost savings and extends the life of Voyage Care\u2019s assets.\nA Culture of Continuous Improvement:\nBy collaborating closely with your teams, we\u2019re excited about the chance to spark a shared enthusiasm for uncovering and pursuing innovative improvements that make a real difference. We believe every innovative idea should be backed by a solid business case, one that carefully weighs the costs of development and implementation against the benefits it promises to the project. This critical assessment happens early on, during the innovation evaluation phase, to ensure we\u2019re on the right track from the start.\nOur approach to innovation is structured yet flexible, designed to measure impact and applicability across four key dimensions:\nStrategic Initiatives: These are big picture ideas with the power to influence beyond the scope of the immediate project, offering long term benefits.\nProject-wide Impact: These initiatives are felt across all sites, bringing uniform improvements and enhancements.\nSite-specific Solutions: Tailored to the unique needs of individual sites, these initiatives address local challenges and opportunities.\nDetailed Innovations: Focused on specific services, these are the nuts and bolts that fine-tune our approach, making every detail count.\nThis multi-layered evaluation ensures that only the most promising and beneficial innovations move forward. It allows us to manage and control the roll out of new ideas efficiently, measuring their impact at every level. Crucially, innovation at Voyage Care isn\u2019t just about novelty; it\u2019s about delivering clear, tangible benefits to the project, ensuring every new idea translates into real-world value.\n6. Quality\n6.1 Customer Care\nIEM Facilities Management pledges an unwavering commitment to Voyage Care, anchored in a suite of customer service guarantees designed to exceed your expectations and support your operations. Central to our promise is the assurance of service availability around the clock, every day of the year, ensuring that Voyage Care\u2019s operations are bolstered by continuous and uninterrupted support. This commitment to 24/7/365 service underscores our recognition of the essential nature of our work together.\nBy anticipating challenges and preparing detailed contingency plans, we aim to ensure that service delivery is not just reactive but anticipatory. Our strategic planning and continuous improvement efforts are manifested in regular planned meetings and annual reviews. These are not mere formalities but vital touch points for collaborative analysis, strategic alignment, and reinforcing our commitment to evolving with Voyage Care\u2019s needs.\nAt the heart of our operational excellence is the AIMS CAFM system, which provides real-time monitoring and swift issue resolution capabilities, ensuring responsiveness to Voyage Care\u2019s needs at all times. This technology, combined with our dedication to regular performance reviews and close collaboration with\n\u201cInnovation and Technology: We embrace innovation and leverage cutting edge technology to drive continuous improvement in our services.\u201d\n13\nVoyage Care, illustrates our commitment to transparency and excellence. We take a proactive approach to service management, anticipating challenges and crafting comprehensive contingency plans to ensure seamless service continuity. Our service model includes assigning dedicated personnel to the Voyage Care account, ensuring a team that is not only familiar with but specialised in your specific operational needs and preferences. This depth of understanding, combined with continuous training and robust feedback mechanisms, ensures our customer care is both personalised and adaptable to the nuances of your operations.\n6.2 Quality of Service\nOur service delivery is meticulously designed around the strict SLA and KPI criteria, ensuring that every aspect of our service not only meets but aims to exceed Voyage Care\u2019s expectations. By systematically tracking performance against these benchmarks, we maintain a high-quality service that is both quantifiable and consistently improving.\nAt IEM, we approach our relationship with Voyage Care as more than just a service provider but as an integrated estate partner, as our name implies. This means that our operational excellence is intricately woven into the fabric of your organisation, aligning seamlessly with your goals and objectives.\nIEM believes in the integration of technology into our service delivery, the backbone of our operational excellence is the advanced use of the AIMS CAFM system. This platform streamlines the management of tasks, from logging to resolution, ensuring efficient and transparent operations. Our approach includes not just digital tracking but also the strategic categorisation of tasks based on urgency and impact, ensuring that resources are optimally allocated to address the most critical needs first.\nThrough weekly briefings, rigorous quality control protocols, and the strategic use of real-time monitoring via the AIMS CAFM system, we ensure that our operational standards are never compromised. These practices allow for a level of service monitoring that is detailed, transparent, and adaptable to immediate and long-term needs.\nOur commitment to quality assurance is thoroughly ingrained in all our operational activity. We leverage our ISO 9001 Quality Management System Accreditation to underpin our quality systems and policies.\nReactive Task - P1 Reactive Task \u2013 P2 Reactive Task - P3 Reactive Task - P4 Quote Approvals Task SLA Timeframe 4-hour attendance 24-hour attendance 5-day attendance 30-day attendance aimed to be completed within 30 days Within SLA Task Updates No updates within 2 hours No updates within 12 hours No updates within 3 Days No updates within 20 Days No updates within 20 Days If the task is within the SLA time frame, please check the notes added to the AiMS system. A note can be added here FIRST to request an update. First level Escalation No attendance within 4 hours No attendance within 24 hours No attendance within 3 Days No attendance within 25 Days No attendance within 25 Days If the task has failed to meet SLAs with NO correspondence, please escalate the issue to the IEM helpdesk at 0203 772 4188 or via email at helpdesk@integrated-em.com. Second level Escalation Task not completed 8 hours Task not completed within 30 hours Task not completed 6 Days Task not completed 35 Days Task not completed 35 Days Raise this task with the internal property manager, who will subsequently coordinate with IEM management regarding the escalation and resolution.\n14\n6.3 Continuous Improvement\nContinuous improvement is not just a goal but a fundamental principle embedded in our approach at IEM. We recognise that the pursuit of excellence is an ongoing journey, and we are committed to continually enhancing our services to better meet the evolving needs of our clients, including Voyage Care.\nOur dedication to continuous improvement is evident in several key areas:\nFeedback Mechanisms: We actively solicit feedback from Voyage Care stakeholders at every opportunity, whether through regular meetings, surveys, or informal discussions. This feedback serves as valuable insight into areas where we excel and areas where we can enhance our services.\nTraining and Development: We invest in the continuous training and development of our team members to ensure they are equipped with the latest skills, knowledge, and best practices in facility management. This includes technical training, customer service workshops, and leadership development programs.\nProcess Optimisation: We regularly review and refine our operational processes to identify inefficiencies and implement improvements. This includes streamlining workflow, optimising resource allocation, and leveraging technology to enhance efficiency and effectiveness.\nPerformance Monitoring: We closely monitor key performance indicators (KPIs) and service level agreements (SLAs) to assess our performance objectively. By analysing performance metrics, we can identify areas for improvement and take proactive measures to address any deviations from expected standards.\nInnovation and Technology: We embrace innovation and leverage cutting-edge technology to drive continuous improvement in our services. This includes the use of advanced facility management systems, IoT devices for predictive maintenance, and digital tools for real-time monitoring and reporting.\nQuality Management Systems: We adhere to rigorous quality management systems, including ISO 9001 certification, to ensure that quality is ingrained in every aspect of our operations. Regular internal audits and external assessments help us maintain the highest standards of quality and compliance.\nIn summary, continuous improvement is not just a buzzword for us; it\u2019s a fundamental aspect of how we operate at IEM. By actively seeking feedback, investing in our team, optimising processes, monitoring performance, embracing innovation, and upholding stringent quality standards, we are committed to delivering ever-improving services to Voyage Care and exceeding their expectation.\n7. Experience\n7.1 Relevant Experience\nIEM brings extensive experience in successfully operating under framework agreements across the UK and Ireland, notably with distinguished partners such as NHS West Suffolk Trust and Arnold Clark.\nWith Arnold Clark, IEM has demonstrated its commitment to excellence through seamless integration into a framework agreement over the past 36 months. Recently renewed for an additional 36 months, this enduring partnership underscores the quality of service provided. During this period, IEM efficiently managed hundreds of reactive tasks on average nationwide. Leveraging a network of safe contractor-approved partners, IEM addressed various disciplines, including plumbing, electrical, HVAC, and roofing. Additionally, IEM completed multiple small to medium projects for Arnold Clark, including internal refurbishments valued between \u00a3120k to \u00a3150k and roof repairs ranging from \u00a320k to \u00a3100k.\nSimilarly, under the framework agreement with NHS West Suffolk Trust, in place for the past 18 months, IEM delivers exceptional reactive and Planned Preventative Maintenance (PPM) services. Integral to this partnership is IEM\u2019s support for the maintenance and ongoing operation of MRI equipment, requiring\n15\nboth reactive interventions and regular PPM for chillers and refrigeration systems crucial to MRI operations. This demonstrates IEM\u2019s commitment to providing specialised and reliable services tailored to the unique needs of its esteemed clientele.\n7.2 Past Performance\nIn reviewing our past performance, one standout achievement is our successful execution of a framework agreement supporting IVC Vetinary practises with reactive work over the past 12 months. This endeavour encompassed managing reactive requirements across IVC\u2019s extensive UK estate, comprising approximately 1200 buildings.\nOur commitment to excellence was evident in adhering meticulously to our service level agreement (SLA) targets, ensuring timely task completion. We aimed to address P1 tasks within a remarkable 4-hour window, followed by P2 tasks within 24 hours, P3 tasks within 5 days, and P4 tasks within 30 days. This precision in service delivery minimised disruption to IVC\u2019s operations while upholding responsiveness and effectiveness.\nKey to our success was the utilisation of a central rate card in collaboration with the client, facilitating streamlined management of the reactive workload. Despite handling 400 to 450 tasks weekly, we maintained efficiency and reliability without encountering any claims throughout the 12-month period.\nTransparency and accountability were paramount, demonstrated through comprehensive weekly and monthly management information reports provided to the client. These reports aided decision-making processes and facilitated a thorough assessment of our performance against agreed SLAs. Weekly operational calls with our dedicated support manager ensured open communication and proactive resolution of emerging challenges.\nThe success of our partnership with IVC is evidenced by our recent agreement to expand collaboration, encompassing not only reactive works but also Planned Preventative Maintenance (PPM) and project works across their entire portfolio.\n8. Closing Remarks\nIn closing, IEM is eager to embark on a collaborative journey with Voyage Care, centred around your unique needs and aspirations. Our commitment to transparency, accountability, and innovation ensures that our partnership will be characterised by open communication, mutual trust, and a shared commitment to excellence.\nBy leveraging advanced technology like the AIMS CAFM system and drawing upon our extensive experience in managing complex frameworks, including our successful collaborations with organisations like Arnold Clark and NHS West Suffolk Trust, we are well-equipped to support Voyage Care in achieving its goals.\nOur tailored approach, designed specifically for Voyage Care as an integrated estate partner, ensures that every aspect of our service delivery is aligned with your objectives. From efficient task management and proactive maintenance to transparent communication and continuous improvement, we are dedicated to delivering service that not only meets but exceeds your expectations.\nAs we move forward together, we are excited about the opportunity to collaborate closely with Voyage Care, sparking innovation, driving efficiency, and delivering tangible value at every step. With IEM Facilities Management as your trusted partner, you can be confident that your facilities are in capable hands, and we are committed to supporting Voyage Care in its mission to provide exceptional care and support.\nVoyage Care\nPrepared by IEM\nDear Chris,\nI trust this message finds you well.\nBefore delving into the specifics of our proposal, I would like to extend my gratitude for considering our offering. At the core of our approach lies a simple yet powerful vision: \u201cSimplify the complexity.\u201d This principle guides us in all our endeavours, aiming to streamline processes and provide seamless solutions.\nAs your integrated estates partner, our mission would be to offer ease and efficiency by leveraging our extensive network of suppliers, providing a comprehensive one-stop solution.\nWe are confident that you will discover the solution you seek within the pages of our proposal. Should you have any questions or require further clarification, please do not hesitate to reach out.\nWarm regards,\nAlistair Scott\n\u201cTrue compassion is more than just feeling for others;\nit is taking action\nto help them.\u201d\nBarack Obama\n4\nTable Of Contents\n1. Costs - Rate Card .....................................................................................................................Submission Folder\n2. Signed Form Of Tender .................................................................................................................................................................... 16\n3. Technical - Capability / Expertise\n3.1 Company background and overview ............................................................................................................ 5\n3.2 CAFM Experience ............................................................................................................................................................................................... 5\n3.3 Account Structure .............................................................................................................................................................................................. 6\n3.4 Back Office Support ...................................................................................................................................................................................... 6\n3.5 Key Management ................................................................................................................................................................................................ 6\n4. Technical Resources\n4.1 Operational Infrastructure and Expertise Overview ............................................ 8\n5. Service Delivery\n5.1 Delivery Approach and Geographic Scope .............................................................................. 8\n5.2 Communication Protocols and CAFM Utilisation .................................................... 9\n5.3 Team Structure .................................................................................................................................................................................................... 10\n5.4 Innovation and Added Value .......................................................................................................................................... 12\n6. Quality\n6.1 Customer Care ........................................................................................................................................................................................................... 12\n6.2 Quality Of Service ........................................................................................................................................................................................... 13\n6.3 Continuous Improvement ........................................................................................................................................................ 14\n7. Experience\n7.1 Relevant Experience .................................................................................................................................................................................. 14\n7.2 Past Performance ............................................................................................................................................................................................. 15\n8. Closing................................................................................................................................................................................................................................................. 15\nInsurance Policies............................................................................................................................ Submission Folder\nSafe Contractor........................................................................................................................................ Submission Folder\nHealth & Safety........................................................................................................................................ Submission Folder\n5\n3. Technical Resources\n3.1 Company Background\nIEM is honoured to submit our tender for your Hard FM Services at Voyager Care, marking the beginning of a partnership aimed at revolutionising facilities management standards. At IEM, we are driven by a singular mission: to simplify the complexities of estate management while delivering unparalleled expertise, innovative solutions, and unwavering excellence.\nWith over 25 years of experience in facilities management, IEM is not just another service provider\u2014we\u2019re your strategic partners in building efficient and thriving estates. Based in Colchester, our team of professionals prioritises your business needs, offering tailored solutions and expert advice whenever required. Supported by an extensive network of 2,000 skilled engineers ensures that we can swiftly address challenges across diverse geographical locations, extending our support far beyond regional boundaries.\nAt the core of IEM\u2019s approach lies a comprehensive Five Point Plan, meticulously crafted to refine operational workflow and boost efficiency. This plan encompasses a deep understanding of assets, insight into their condition,
  adherence to compliance standards, clarity in prioritising objectives, and excellence in delivery management. Through strategic planning and continuous improvement efforts, we ensure that every goal is met with precision and effectiveness.\nOur commitment to Voyage Care goes beyond just providing services; it\u2019s about fostering collaboration, open and honest communication, and mutual trust. Like Voyage Care, we champion a people centric approach, collaboration, trust, exceptional outcomes, and equity for everyone. This alignment forms the foundations of our partnership, ensuring that our collaboration yields meaningful results.\nAs part of our service model, we employ dedicated personnel who specialise in your estate\u2019s specific operational needs and preferences. This tailored approach, combined with continuous training and robust feedback mechanisms, guarantees personalised and adaptable customer care.\nMoreover, our dedication to corporate social responsibility extends into the communities where Voyage Care operates. Through initiatives such as volunteer programs, charitable donations, and sponsorships, we support vital causes such as Care after Combat and the Armed Forces Covenant, making a positive impact on those who have served our country. As an accredited Real Living Wage employer, we ensure fair compensation for all our staff. Our dedication to corporate social responsibility extends into the communities where Voyage Care operates, with initiatives such as volunteer programs and charitable donations making a positive impact.\nIn conclusion, IEM is fully committed to supporting Voyage Care\u2019s mission by delivering tailored, high-quality services backed by expertise, innovation, and a people first approach. Together, through collaboration, open and honest communication, we can achieve remarkable outcomes and make a meaningful difference in the lives of those we serve.\n3.2 CAFM Experience\nWe proudly embrace cutting-edge technology to elevate the efficiency and effectiveness of our service delivery. Central to our delivery is the integration of the 24-hour help desk and the AiMS CAFM system, which together ensure seamless operations and communication. The around-the-clock availability of our technical help desk guarantees you have immediate support and assistance, day or night. This unwavering support is instrumental in maintaining operational continuity and reducing any disruptions to daily activities, providing peace of mind and reliability.\nFurthermore, the AiMS CAFM system stands as a pillar of our technological strategy, offering real-time data on asset performance, maintenance schedules, compliance statuses, and more. This system not only streamlines facility management processes but also enhances\n\u201cStrategic partners in building efficient and\nthriving estates.\u201d\n6\ndecision-making and resource allocation. With the ability to monitor work orders, manage maintenance tasks, and ensure service delivery transparency in real-time, we set a new standard for accountability and efficiency in contract delivery.\n3.3 Account Structure\nIEM\u2019s mobilisation team will engage closely with Voyage Care to meticulously prepare for a flawless launch and integration. We understand the significant impact of maintaining consistency and offer the assurance of having an experienced and knowledgeable team in place throughout all pivotal phases, including the transition to business as usual.\nTo facilitate a smooth implementation and migration, our Operations Manager, Implementation Specialists, Technical Services Manager and Client Account Manager will be integral, providing steadfast support and expertise. This team will not only be a constant during the mobilisation phase but will also ensure stability and continuity as we shift into regular operations.\nIEM is committed to your success beyond the initial phase, offering a detailed service review 100 days post-implementation. This critical assessment will evaluate service performance, responsiveness to the dynamic needs of the facility, and the effectiveness of integration into everyday operations. We will identify opportunities for improvements and refinements, ensuring the services we provide are perfectly attuned to Voyage Care\u2019s strategic objectives and are delivered seamlessly as part of our ongoing partnership.\n3.4 Back Office Support\nOur back-office support encompasses a wide range of functions essential for delivering exceptional service to Voyager Care. This includes expertise in HR, Supplier Management, Quality, Health, Safety, and Environment (QHSE), as well as optional services like Energy Management and Asset Management. These functions collectively ensure that our operations are optimised, compliant, and aligned with industry best practices. Our HR team ensures that our staff are well-trained and motivated, while Supplier Management ensures strong relationships with external partners. Quality, Health, Safety, and Environment (QHSE) protocols are rigorously enforced by our dedicated team to mitigate risks and ensure compliance.\nOptional services like Energy Management can optimise energy usage and efficiency, while Asset Management ensures proper maintenance and management of equipment. Together, these functions form the backbone of our operations, enabling us to deliver a high standard of service to Voyager Care.\n3.5 Key Management Personnel\nJoe Benitez\nOur Managing Director Joe, has been an integral part of our company since its inception, overseeing all aspects of the business with a strong focus on Continuous Improvement principles and Operational Efficiency. With a background spanning 25 years in Retail, Joe has held national roles with renowned companies such as Staples, Homebase, IKEA, and Curry\u2019s, among others. His final retail position was as Group Commercial Director for the Dixons Carphone Group, where he spearheaded initiatives to enhance the product and services customer journey, prioritising customer centricity in operational processes. Prior to joining IEM, Joe served as the Group Business Development Director for CloudFM, where he played a pivotal role in driving innovation, earning the company the distinction of being the first FM company to win the Queens Award for Innovation.\nChristy Smith\nChristy, our Operations Manager oversees diverse departments including Help desk, Supply Chain, and Quotations. With over ten years in Facilities Management (FM), she started as a Help desk professional, advancing steadily. Her experience includes notable clients such as Pizza Express, Poundland, and IVC. Holding a Level 4 certificate from IWFM and an ILM Level 3 Diploma in Facilities & Management, Christy continuously enhances her expertise. During her tenure at IEM, she contributed to its growth, evolving from a single department to specialist teams. Previously, as a Senior Account Manager, she honed skills in client management and strategic planning, with roles at CloudFM providing insights into operational excellence and leadership.\n7\nJamie Franklin\nA versatile professional with a unique blend of animation and facilities management expertise. Graduating with an Animation Degree in 2014, Jamie embarked on a career journey that initially delved into retail management through a graduate program at BHS. However, driven by a passion for technical innovation, Jamie transitioned into facilities management in 2017, concurrently undertaking an electromechanical qualification. Joining a prestigious high-end residential business, Jamie quickly ascended the ranks, leveraging management skills to oversee compliance processes and develop a keen passion for energy conservation. Serving as Technical Services Manager at IEM since June 2023, Jamie leads the compliance department, ensuring regulatory adherence while spearheading technical projects with clients. Jamie\u2019s expertise extends to energy management, collaborating closely with clients to optimise energy consumption, enhance asset performance, and reduce environmental impact. With a strategic mindset and a commitment to excellence, Jamie Franklin continues to drive innovation and deliver impactful solutions in technical services and facilities management.\nGoda Tamosiuniene\nHailing from Lithuania, brings a wealth of experience in leisure and tourism to her role as Compliance Manager at IEM. Having transitioned into Facilities Management, she has honed her skills in statutory compliance, asset management, and maintenance processes during her tenure at a prestigious high-end residential company. Joining IEM in July 2023, Goda plays a pivotal role in fortifying the company\u2019s compliance proposition. Her dedication to seamless delivery of statutory PPMs and commitment to client satisfaction distinguish her as a trusted leader in facilities management. Leveraging her expertise, she elevates compliance standards and operational efficiencies, driving positive outcomes for IEM\u2019s clients.\nZsuzsanna Banfi\nOur Supply Chain Lead, brings extensive expertise to her role, overseeing partner mobilisation and performance monitoring. With a background in Operations Management and Supply Chain/Procurement, her strategic approach and attention to detail drive significant impact. Holding a Level 2 Customs Practice and Procedure Award from the UK Customs Academy, she ensures compliance in global trade. Additionally, her Level 5 Advanced Diploma in Supply Chain Management streamlines processes and manages risks. Zsuzsanna\u2019s bachelor\u2019s degree in economics, with a specialisation in Tourism and Hotel Management, enhances insights into economic principles.\nCasey Staff\nOne of the Senior Customer Care Representatives at IEM, Casey commenced her journey on the Help desk in September 2022. This marks her introduction to the Facilities Management sector, following previous roles as a Sales Associate and Office Administrator. She holds a bachelor\u2019s in international business from the University of Brighton, supplemented by a year of studying abroad in Turin, Italy, where she acquired a beginner level of proficiency in Italian. Currently, Casey continues to pursue language studies in both Italian and Dutch while exploring IWFM courses to expand her knowledge. With a keen interest in Projects and Marketing, she aspires to pursue a master\u2019s degree in the near future.\nBeatrice Sandor-Sulutiu\nOur Benchmark Analyst, brings a wealth of experience in estimating to our team, promising to greatly enhance our collaboration with valued partners like yourselves, as well as with our clients. With over five years of extensive experience in estimating and a background in project management and human resources, Beatrice is well-equipped to contribute effectively to our operations. She holds a bachelor\u2019s degree in creative writing, showcasing her diverse skill set and adaptability. Beatrice\u2019s professional journey includes roles as an HR Manager for an Amazon Delivery Partner, and positions as an estimator at Mumford and Wood, AGM, and Delta T, where she consistently delivered high-quality work.\n8\n4. Technical Resources\n4.1 Operational Infrastructure and\nExpertise Overview\nInitiating our partnership with Voyage Care, IEM would\nbe fully equipped to deliver exceptional service with a\ndedicated mobilisation team and a robust workforce\nof qualified engineers. During the mobilisation phase,\nwe conduct comprehensive site visits to familiarise\nourselves with Voyage Care\u2019s estate, ensuring a thorough\nunderstanding of your unique needs and environments.\nOur team comprises a diverse range of skilled engineers,\neach holding essential qualifications such as NVQ Level 3\nin Engineering Maintenance, City & Guilds qualifications\nin Electrical and Mechanical Engineering, and Health &\nSafety certifications like IOSH or NEBOSH. This ensures\nthat every engineer serving Voyage Care\u2019s needs is highly\nqualified and specialised in their respective fields.\nWhile we maintain a core team of engineers, we\nalso leverage a strategic subcontracting strategy to\ncomplement our workforce and enhance service delivery.\nOur extensive national presence allows us to tap into a\nvast network of subcontractors, ensuring efficient and\nreliable service across all your facilities.\nTransparency and alignment with Voyage Care are\nparamount in our service delivery approach. We allocate\ndedicated Help desk members to your account, extensively\ntrained to become experts in your specific needs, ensuring\ncontinuity and consistency in service delivery.\nFurthermore, our commitment to quality is reflected\nin our strict quality control protocols, ensuring that\nour services not only meet but exceed Service Level\nAgreements (SLAs) and Key Performance Indicators\n(KPIs).\nRegular monthly engagement with Voyage Care\nstakeholders for feedback enables us to continuously\nrefine our services to align with your evolving needs and\nmaintain a service standard that mirrors Voyage Care\u2019s\nhigh expectations.\nWe ensure transparency and accountability through\ndetailed weekly and monthly management reports\ndelivered through our advanced CAFM system.\nThese reports cover reactive, Planned Preventative\nMaintenance (PPM), and project tasks, providing insights\ninto SLAs, KPIs, and overall performance.\nOur compliance process follows strict industry standards\noutlined in the SFG20 procedures, ensuring timely and\nbest-practice delivery. Thorough risk assessments and\nmethod statements are conducted prior to any work,\nprioritising safety and efficiency.\nIn conclusion, our approach emphasises precision,\nthoroughness, and transparency, setting the standard\nfor excellence in service delivery and compliance\nmanagement within the industry.\n5. Service Delivery\n5.1 Delivery Approach and Geographic\nScope\nAs we embark on our partnership journey with Voyage\nCare, IEM Facilities Management is prepared to deploy\na dedicated mobilisation team from the onset through\nto the 100-day review milestone. Our foundational\nbelief is that an intimate understanding of your unique\nrequirements and environments is pivotal to delivering\nexceptional service. During the mobilisation phase, our\npriority lies in conducting comprehensive site visits to\nfully acquaint ourselves with every aspect of your estate.\nThis immersive process extends beyond mere\nfamiliarisation; it entails absorbing the unique operations\nthat defines Voyage Care, ensuring our Help desk\nteam is not only well-versed in your layout but also\ndeeply attuned to your operations. This thorough initial\nexploration serves as the basis for crafting a bespoke\n\u201cClient Manual,\u201d a living document that evolves to\naccurately reflect the evolving landscape of your estate.\nBeyond mobilisation, we place significant emphasis on\ncontinuous training and communication to keep our team\ninformed of any developments or changes within Voyage\nCare\u2019s operations. This includes regular refresher training\nsessions, knowledge-sharing forums, and ongoing\nGB & I\nCoverage\n9\n\u201cIEM\u2019s Commitment to Excellence from Day One to Beyond: Customised Solutions, Unwavering Quality and Strategic Partnerships\u201d\nfeedback mechanisms to promptly address any potential issues or areas for improvement.\nTo maintain a consistently high standard of service across all communication channels, we assign dedicated Help desk members to the Voyage Care account. Through focused, extensive training, these individuals become experts in your specific needs, ensuring seamless continuity and consistency in service delivery.\nAt IEM, our service approach for Voyage Care is underpinned by our extensive national presence and a strategic subcontracting strategy, ensuring efficient, reliable, and high-quality service delivery across all your facilities. Our ultimate objective is to meet your bespoke needs with excellence at every juncture, setting new benchmarks in facility management. We prioritise transparency and alignment with Voyage Care through regular updates on ongoing projects, outstanding works, and preferences, facilitated by our AIMS CAFM system for real-time service monitoring and management.\nRegarding on-site routine maintenance, our focus remains squarely on you, ensuring smooth, uninterrupted operations during normal business hours. We collaborate closely with you to develop tailored maintenance schedules that align precisely with your requirements. These custom maintenance plans incorporate preventive measures aimed at minimising downtime and extending the lifespan of your equipment and facilities. Our commitment to delivering superior service extends to compliance with industry standards, including the use of CIPSE, SFG 20, and other recognised best practices in our maintenance protocols.\nMonthly engagement with Voyage Care stakeholders for feedback forms a central component of our process, enabling us to continuously refine our services in alignment with your evolving needs and maintaining a service standard that mirrors Voyage Care\u2019s high expectations.\nIn terms of compliance audits and reporting, our standard procedures include reviews of compliance portals, weekly team meetings with predefined agendas, weekly MI reports through the CAFM system, monthly compliance audits, and QHSE audits. Any findings from these audits are promptly shared with you to ensure transparency and accountability.\nAll performance management elements are underpinned by our company-wide integrated management system, certified to various ISO standards including ISO 9001, ISO 14001, and ISO 45001. This ensures a minimum benchmark of best practice across all areas of our service delivery.\n5.2 Communication Protocols and CAFM Utilisation\nIEM is fully committed to delivering outstanding service to Voyage Care, with effective communication and strategic use of the AIMS CAFM system. Our approach ensures streamlined task management and efficient handling of issues from initiation to resolution. We offer comprehensive support through phone, email, and direct engagement via the AIMS CAFM platform.\nIn developing our robust escalation procedures, we work together with you to tailor these processes to your unique needs. This bespoke strategy ensures a transparent and accountable method for issue management, highlighting efficiency and clear communication.\nTo uphold a consistent service level, we assign dedicated Help desk members to the your account, who undergo extensive training to specialise in your operations, guaranteeing continuity and consistency in service delivery. Your Account Manager plays a crucial role in contract management and in providing responsive service, facilitated by regular, structured meetings and proactive communication, ensuring a seamless service experience.\nOur methodical approach extends to the management and submission of all completion documentation, ensuring accuracy, compliance, and efficiency. From reviewing documents to integrating compliance certification with the CAFM system, our process guarantees that every piece of documentation adheres to stringent standards.\nThis meticulous attention to detail, alongside our commitment to continuous improvement and regular quality audits, means service delivery to Voyage Care not only meets but surpasses SLAs and KPIs, aligning perfectly with your evolving standards.\nOur communication strategy is intentionally designed to align with your objectives, employing:\nWeekly Calls\nScheduled discussions with Voyage Care representatives to update on progress, address concerns, and align on objectives.\nComprehensive Weekly Reports\nTailored reports offering insights into performance metrics, issue resolution, and actions taken, ensuring you are always informed and in control.\nAIMS CAFM System\nStreamlined documentation management ensuring\n10\ntransparent access to maintenance records, risk\nassessments, and compliance certificates, keeping you\nfully informed.\nCompliance and Quality Assurance\nUtilising AIMS to manage and verify compliance, providing\npeace of mind with comprehensive documentation and\nsecure access to all project-related information.\nTask Priorities\nOur escalation plan is designed to prioritise issues based\non their severity and potential impact on Voyage Care\u2019s\noperations. From life-threatening situations to non-urgent\nrequests, our categorisation ensures a tailored response\nthat aligns with the urgency of each situation.\nPriority 1: Guaranteeing an immediate 4-hour response\nand resolution within the shortest possible time frame.\nSituations with potential safety hazards or impacting\nbusiness operations\nPriority 2: Ensuring an on-site response within 24 hours\nduring business hours.\nPriority 3: Issues that do not impede business operations\nor pose safety risks fall under with attendance guaranteed\nwithin 5 days.\nPriority 4: Non-urgent requests with a commitment to\nrespond within 30 days.\nThrough these strategies, IEM ensures a partnership with\nVoyage Care that is built on trust, transparency, and a\nmutual commitment to excellence.\nExample of client site comms pieces\n5.3 Team Structure\nIEM presents a specialised team for the Voyage\nCare project, meticulously structured to provide\ncomprehensive Facilities Management (FM) services.\nOur team is adeptly led by Joe Benitez, Managing\nDirector, who brings strategic oversight and a wealth\nof FM and retail sector expertise. Joe will oversee the\noverall management and strategic direction of the\ncontract.\nChristy Smith, serving as Operations Manager, is pivotal\nin the management of day-to-day operations. Her\nextensive experience in FM, underpinned by IWFM and\nILM certifications, ensures effective service delivery and\ncoordination across key operational areas, including the\nHelp desk, Supply Chain, and Quotations.\nJamie Franklin, our Technical Services Manager, enhances\nthe team with his deep-rooted electric\u00e5al engineering\nbackground. Since his start in early 2023, he has actively\ncontributed to elevating our technical service provisions,\nwith a focus on compliance and energy management,\nfortifying our commitment to innovation.\nCasey Staff, our Senior Customer Care Representative,\nexcels in client engagement and resolution management.\nHer background in International Business and\ncommitment to ongoing professional development\nare integral to her role in delivering superior customer\nservice.\nGoda Tamosiuniene, the Compliance Manager,\nbrings over a decade of FM experience to the table,\nensuring adherence to all regulatory requirements and\nmaintenance protocols, thereby safeguarding operational\nintegrity.\nZsuzsanna Banfi, leading our Supply Chain efforts,\nmanages partner relations and supply chain efficacy,\ndrawing upon her expertise in Operations Management\nand Procurement to optimize our processes.\nBeatrice Sandor Sulutiu, as Benchmark Analyst, oversees\nthe issuance of quotes, applying her construction\nindustry experience to align with client expectations and\nproject needs accurately.\nOur proposal encapsulates a team of select professionals,\neach chosen for their specific skill set to ensure a holistic\nand bespoke approach to the Voyage Care project. They\nrepresent the core of our broader team of professionals,\nensuring a coordinated effort to achieve project\nobjectives and service.\n11\nIEM 2024 Organisation Chart\n12\n5.4 Innovation and Added Value\nAt IEM, our commitment to delivering exceptional facility management services for Voyage Care is underpinned by a relentless pursuit of innovation and a culture of adding value. We\u2019re not just about meeting expectations; we\u2019re about redefining them through a blend of cutting-edge solutions, transparent operations, and forward-thinking strategies.\nLeveraging Technology for Efficiency:\nThe heart of our operation lies in the use of the AIMS CAFM system. This powerful platform is our command centre, facilitating task management, progress tracking, and seamless communication through phone, email, and directly within AIMS. It\u2019s designed for efficiency, enabling us to respond swiftly to Voyage Care\u2019s needs with real-time updates and detailed tracking of all activities on site.\nTransparent Communication and Informed Decision Making:\nClear and open communication is a cornerstone of our service delivery. Through regular updates, detailed weekly reports, and ongoing briefings, we keep Voyage Care in the loop at every stage. This ensures that you\u2019re always informed, engaged, and in control.\nProactive Maintenance for Operational Excellence:\nOur approach extends beyond fixing problems as they arise. We anticipate them, using predictive analytics and preventive maintenance to identify and address potential issues before they impact operations. This not only ensures smoother day-to-day operations but also contributes to cost savings and extends the life of Voyage Care\u2019s assets.\nA Culture of Continuous Improvement:\nBy collaborating closely with your teams, we\u2019re excited about the chance to spark a shared enthusiasm for uncovering and pursuing innovative improvements that make a real difference. We believe every innovative idea should be backed by a solid business case, one that carefully weighs the costs of development and implementation against the benefits it promises to the project. This critical assessment happens early on, during the innovation evaluation phase, to ensure we\u2019re on the right track from the start.\nOur approach to innovation is structured yet flexible, designed to measure impact and applicability across four key dimensions:\nStrategic Initiatives: These are big picture ideas with the power to influence beyond the scope of the immediate project, offering long term benefits.\nProject-wide Impact: These initiatives are felt across all sites, bringing uniform improvements and enhancements.\nSite-specific Solutions: Tailored to the unique needs of individual sites, these initiatives address local challenges and opportunities.\nDetailed Innovations: Focused on specific services, these are the nuts and bolts that fine-tune our approach, making every detail count.\nThis multi-layered evaluation ensures that only the most promising and beneficial innovations move forward. It allows us to manage and control the roll out of new ideas efficiently, measuring their impact at every level. Crucially, innovation at Voyage Care isn\u2019t just about novelty; it\u2019s about delivering clear, tangible benefits to the project, ensuring every new idea translates into real-world value.\n6. Quality\n6.1 Customer Care\nIEM Facilities Management pledges an unwavering commitment to Voyage Care, anchored in a suite of customer service guarantees designed to exceed your expectations and support your operations. Central to our promise is the assurance of service availability around the clock, every day of the year, ensuring that Voyage Care\u2019s operations are bolstered by continuous and uninterrupted support. This commitment to 24/7/365 service underscores our recognition of the essential nature of our work together.\nBy anticipating challenges and preparing detailed contingency plans, we aim to ensure that service delivery is not just reactive but anticipatory. Our strategic planning and continuous improvement efforts are manifested in regular planned meetings and annual reviews. These are not mere formalities but vital touch points for collaborative analysis, strategic alignment, and reinforcing our commitment to evolving with Voyage Care\u2019s needs.\nAt the heart of our operational excellence is the AIMS CAFM system, which provides real-time monitoring and swift issue resolution capabilities, ensuring responsiveness to Voyage Care\u2019s needs at all times. This technology, combined with our dedication to regular performance reviews and close collaboration with\n\u201cInnovation and Technology: We embrace innovation and leverage cutting edge technology to drive continuous improvement in our services.\u201d\n13\nVoyage Care, illustrates our commitment to transparency and excellence. We take a proactive approach to service management, anticipating challenges and crafting comprehensive contingency plans to ensure seamless service continuity. Our service model includes assigning dedicated personnel to the Voyage Care account, ensuring a team that is not only familiar with but specialised in your specific operational needs and preferences. This depth of understanding, combined with continuous training and robust feedback mechanisms, ensures our customer care is both personalised and adaptable to the nuances of your operations.\n6.2 Quality of Service\nOur service delivery is meticulously designed around the strict SLA and KPI criteria, ensuring that every aspect of our service not only meets but aims to exceed Voyage Care\u2019s expectations. By systematically tracking performance against these benchmarks, we maintain a high-quality service that is both quantifiable and consistently improving.\nAt IEM, we approach our relationship with Voyage Care as more than just a service provider but as an integrated estate partner, as our name implies. This means that our operational excellence is intricately woven into the fabric of your organisation, aligning seamlessly with your goals and objectives.\nIEM believes in the integration of technology into our service delivery, the backbone of our operational excellence is the advanced use of the AIMS CAFM system. This platform streamlines the management of tasks, from logging to resolution, ensuring efficient and transparent operations. Our approach includes not just digital tracking but also the strategic categorisation of tasks based on urgency and impact, ensuring that resources are optimally allocated to address the most critical needs first.\nThrough weekly briefings, 
  rigorous quality control protocols, and the strategic use of real-time monitoring via the AIMS CAFM system, we ensure that our operational standards are never compromised. These practices allow for a level of service monitoring that is detailed, transparent, and adaptable to immediate and long-term needs.\nOur commitment to quality assurance is thoroughly ingrained in all our operational activity. We leverage our ISO 9001 Quality Management System Accreditation to underpin our quality systems and policies.\nReactive Task - P1 Reactive Task \u2013 P2 Reactive Task - P3 Reactive Task - P4 Quote Approvals Task SLA Timeframe 4-hour attendance 24-hour attendance 5-day attendance 30-day attendance aimed to be completed within 30 days Within SLA Task Updates No updates within 2 hours No updates within 12 hours No updates within 3 Days No updates within 20 Days No updates within 20 Days If the task is within the SLA time frame, please check the notes added to the AiMS system. A note can be added here FIRST to request an update. First level Escalation No attendance within 4 hours No attendance within 24 hours No attendance within 3 Days No attendance within 25 Days No attendance within 25 Days If the task has failed to meet SLAs with NO correspondence, please escalate the issue to the IEM helpdesk at 0203 772 4188 or via email at helpdesk@integrated-em.com. Second level Escalation Task not completed 8 hours Task not completed within 30 hours Task not completed 6 Days Task not completed 35 Days Task not completed 35 Days Raise this task with the internal property manager, who will subsequently coordinate with IEM management regarding the escalation and resolution.\n14\n6.3 Continuous Improvement\nContinuous improvement is not just a goal but a fundamental principle embedded in our approach at IEM. We recognise that the pursuit of excellence is an ongoing journey, and we are committed to continually enhancing our services to better meet the evolving needs of our clients, including Voyage Care.\nOur dedication to continuous improvement is evident in several key areas:\nFeedback Mechanisms: We actively solicit feedback from Voyage Care stakeholders at every opportunity, whether through regular meetings, surveys, or informal discussions. This feedback serves as valuable insight into areas where we excel and areas where we can enhance our services.\nTraining and Development: We invest in the continuous training and development of our team members to ensure they are equipped with the latest skills, knowledge, and best practices in facility management. This includes technical training, customer service workshops, and leadership development programs.\nProcess Optimisation: We regularly review and refine our operational processes to identify inefficiencies and implement improvements. This includes streamlining workflow, optimising resource allocation, and leveraging technology to enhance efficiency and effectiveness.\nPerformance Monitoring: We closely monitor key performance indicators (KPIs) and service level agreements (SLAs) to assess our performance objectively. By analysing performance metrics, we can identify areas for improvement and take proactive measures to address any deviations from expected standards.\nInnovation and Technology: We embrace innovation and leverage cutting-edge technology to drive continuous improvement in our services. This includes the use of advanced facility management systems, IoT devices for predictive maintenance, and digital tools for real-time monitoring and reporting.\nQuality Management Systems: We adhere to rigorous quality management systems, including ISO 9001 certification, to ensure that quality is ingrained in every aspect of our operations. Regular internal audits and external assessments help us maintain the highest standards of quality and compliance.\nIn summary, continuous improvement is not just a buzzword for us; it\u2019s a fundamental aspect of how we operate at IEM. By actively seeking feedback, investing in our team, optimising processes, monitoring performance, embracing innovation, and upholding stringent quality standards, we are committed to delivering ever-improving services to Voyage Care and exceeding their expectation.\n7. Experience\n7.1 Relevant Experience\nIEM brings extensive experience in successfully operating under framework agreements across the UK and Ireland, notably with distinguished partners such as NHS West Suffolk Trust and Arnold Clark.\nWith Arnold Clark, IEM has demonstrated its commitment to excellence through seamless integration into a framework agreement over the past 36 months. Recently renewed for an additional 36 months, this enduring partnership underscores the quality of service provided. During this period, IEM efficiently managed hundreds of reactive tasks on average nationwide. Leveraging a network of safe contractor-approved partners, IEM addressed various disciplines, including plumbing, electrical, HVAC, and roofing. Additionally, IEM completed multiple small to medium projects for Arnold Clark, including internal refurbishments valued between \u00a3120k to \u00a3150k and roof repairs ranging from \u00a320k to \u00a3100k.\nSimilarly, under the framework agreement with NHS West Suffolk Trust, in place for the past 18 months, IEM delivers exceptional reactive and Planned Preventative Maintenance (PPM) services. Integral to this partnership is IEM\u2019s support for the maintenance and ongoing operation of MRI equipment, requiring\n15\nboth reactive interventions and regular PPM for chillers and refrigeration systems crucial to MRI operations. This demonstrates IEM\u2019s commitment to providing specialised and reliable services tailored to the unique needs of its esteemed clientele.\n7.2 Past Performance\nIn reviewing our past performance, one standout achievement is our successful execution of a framework agreement supporting IVC Vetinary practises with reactive work over the past 12 months. This endeavour encompassed managing reactive requirements across IVC\u2019s extensive UK estate, comprising approximately 1200 buildings.\nOur commitment to excellence was evident in adhering meticulously to our service level agreement (SLA) targets, ensuring timely task completion. We aimed to address P1 tasks within a remarkable 4-hour window, followed by P2 tasks within 24 hours, P3 tasks within 5 days, and P4 tasks within 30 days. This precision in service delivery minimised disruption to IVC\u2019s operations while upholding responsiveness and effectiveness.\nKey to our success was the utilisation of a central rate card in collaboration with the client, facilitating streamlined management of the reactive workload. Despite handling 400 to 450 tasks weekly, we maintained efficiency and reliability without encountering any claims throughout the 12-month period.\nTransparency and accountability were paramount, demonstrated through comprehensive weekly and monthly management information reports provided to the client. These reports aided decision-making processes and facilitated a thorough assessment of our performance against agreed SLAs. Weekly operational calls with our dedicated support manager ensured open communication and proactive resolution of emerging challenges.\nThe success of our partnership with IVC is evidenced by our recent agreement to expand collaboration, encompassing not only reactive works but also Planned Preventative Maintenance (PPM) and project works across their entire portfolio.\n8. Closing Remarks\nIn closing, IEM is eager to embark on a collaborative journey with Voyage Care, centred around your unique needs and aspirations. Our commitment to transparency, accountability, and innovation ensures that our partnership will be characterised by open communication, mutual trust, and a shared commitment to excellence.\nBy leveraging advanced technology like the AIMS CAFM system and drawing upon our extensive experience in managing complex frameworks, including our successful collaborations with organisations like Arnold Clark and NHS West Suffolk Trust, we are well-equipped to support Voyage Care in achieving its goals.\nOur tailored approach, designed specifically for Voyage Care as an integrated estate partner, ensures that every aspect of our service delivery is aligned with your objectives. From efficient task management and proactive maintenance to transparent communication and continuous improvement, we are dedicated to delivering service that not only meets but exceeds your expectations.\nAs we move forward together, we are excited about the opportunity to collaborate closely with Voyage Care, sparking innovation, driving efficiency, and delivering tangible value at every step. With IEM Facilities Management as your trusted partner, you can be confident that your facilities are in capable hands, and we are committed to supporting Voyage Care in its mission to provide exceptional care and support."



  REQUEST FOR INFORMATION \u2013 MEBF Maintenance for Osborne Clarke LLP\nMEBF Tender \u2013 Hard Services Provision for Osborne Clarke (OC), RFI issued by IM&SS Ltd.\nSite Addresses\nLondon \u2013 One London Wall, Barbican, London, EC2Y 5EB\nBristol \u2013 Halo, Counter slip, Bristol, BS1 6AJ\nReading \u2013 3, 23 The Forbury, Forbury Road, Reading, RG1 3JH\nDate of Issue: 8th November 2023\nContractors RFI Submission Deadline: 17.00 \u2013 Friday 17th November 2023\nSubmission by email to: - keith.parker@imassltd.com\nAbout\nOsborne Clarke LLP is an international legal practice headquartered in London, England with offices in the United Kingdom, Germany, Italy, Belgium, Spain, Sweden, France, the Netherlands, China, Hong Kong, India, Singapore, and the United States. The firm has over 270 partners and 1,600 employees spread across its 26 offices around the world.\nOutline Contract Scope\nWithin the contract scope, the selected service provider will be entrusted with delivering a range of hard FM services. Broadly outlined as the following: -\nM&E\n\u2022\nPlanned & reactive maintenance of the mechanical & electrical services.\n\u2022\nPlanned and reactive maintenance of domestic water and drainage systems\n\u2022\nPlanned and reactive maintenance to life safety systems\n\u2022\nPortable appliance testing\n\u2022\nAsset validation and condition reporting\n\u2022\nProvision and management of the CAFM platform\n\u2022\nManagement of specialist subcontractors\n\u2022\nAsset Life cycle analysis and management\n\u2022\nEnergy monitoring and management\n\u2022\nEnvironmental management\n\u2022\nLegislation compliance\nBuilding Fabric\n\u2022\nRepair and maintenance of internal structures \u2013 walls, ceilings etc\n\u2022\nRepair and maintenance to internal flooring and coverings\n\u2022\nRepair and maintenance to internal doors, blinds and windows\n\u2022\nRepair and maintenance of fire doors and passive fire stopping.\nThe successful service provider will be expected to submit monthly reports to transparently outline their service performance against the contractual SLA\u2019s and KPI\u2019s. Effective and regular communication, as well as coordination with the client's designated point of contact, are deemed as being pivotal aspects of this service provision. Furthermore, OC LLP encourage service providers to proactively suggest and adopt environmentally friendly practices as part of the service delivery and will be a key focus point as the new contract progresses.\nGuidance notes for the completion of the RFI\nThe purpose of this RFI is to provide Osborne Clarke LLP with sufficient information about potential Suppliers to allow an assessment to be made of their capability and suitability to be included into a shortlist who will be invited to tender for the contract.\nYou must answer all questions fully.\nAll questions should be answered in English. The questions require concise, honest, and factual responses. Please note where a maximum word limit applies to a section of the form, please adhere to this limit.\nWhere you need to draw attention to a separate document included as part of your response to answer a question, please ensure you provide clarity of which document, which page, and which paragraph/sentence you are drawing attention to.\nEach question must be answered in full using the same section and numbering format as appears in the RFI.\nShould you have any queries regarding this RFI or require any assistance please submit your question by e-mailing the following address:\nkeith.parker@imassltd.com\nEvaluation Criteria RFI Evaluation (Questions Answered Fully) Evaluation Criteria Pass/Fail A - Company Information Pass/Fail B - Financial Information Pass/Fail C - Insurance Pass/Fail (Scored) D - Technical Capacity and Resource Pass/Fail (Scored) E - Quality and Standards Pass/Fail (Scored) F - Health and Safety Pass/Fail (Scored) G - Equality and Diversity Pass/Fail H - Declaration\nOC LLP intends to shortlist 3 highest ranked Suppliers to be selected for Invitation to Tender (RFP).\nSECTION A: COMPANY INFORMATION & STRUCTURE\nA1. Name of Company/organisation making application.\nIntegrated Estate Management Ltd A2. Trading name if different from above.\nIEM A3. Key contact details (within the Supplier). Please note that this will be the address and person all correspondence will be addressed to regarding this RFI and resultant RFP if successful to be shortlisted. Name:\nAlistair Scott Position within organisation:\nFounder Address:\nWeston Business Centre\nHawkins Road\nColchester\nEssex\nCO2 8JX Telephone:\n020 3772 4188 Mobile Phone:\n07827914166 E-mail:\nAlistair.scott@integrated-em.com Web Site:\nhttps://integrated-em.com\nA4. Registered office (if different from above).\nOffice 5, Boleyn Suite,\nHever Road,\nEdenbridge\nKent,\nTN8 7NP\nA5. Are you or is your organisation a: Sole Trader?\nPartnership?\nPrivate Limited Company?\nYes Public limited Company?\nRegistered Charity?\nOther?\nPlease Specify?\nA6. Limited Companies Please state the companies date of incorporation and registration number under the Companies Act 1985. OR\nDate\n02/11/2018\nRegistration Number\n11657337\nDate of registration and the company's registration number under the Industrial and Provident Societies Acts 1965 to 1978. OR\nDate\nNumber\nPartnerships Please state the date the partnership was formed, began trading and Total number of partners. Are the partnerships being a member of a group? If \u201cYes,\u201d detail other relationships within the group and comment on the group structure. OR\nDate\nNumber\nTotal Number of Partners\nAdditional Comments\nSole Trader\nDate\nDate when Supplier began trading\nA7. If the Supplier is a member of a group of companies or subsidiary of another company as defined by Section 736 (1) of the Companies Act 1985, give the names and company numbers of the holding company and any companies in-between you and the holding company, clearly stating the relationship with your organisation.\nCompany Name\nCompany Number\nRelationship\nN/A\nA8. Is the parent company or ultimate holding company prepared to guarantee the performance of the Supplier?\nYes:\nNo:\nN/A\nIf yes, please provide: Name of Company\nRegistration number\nRelationship with your company\nA9. What is your organisation\u2019s VAT number?\n310404272\nSECTION B: FINANCIAL INFORMATION & REFERENCE INFORMATION\nB1 Name of Bankers:\nSantander Address of Bankers:\n2 Triton Square,\nRegents Place\nLondon,\nNW1 3AN Name of Auditors:\nN/A\nB2. Please provide details of the past three years turnover of the company Year Ending 2019 - 20\n\u00a3122,000\nYear Ending 2020 - 21\n\u00a3681,000\nYear Ending 2021 - 22\n\u00a31,174,000\nB3. Please provide details of three existing customers with similar contracts that we can contact for references.\nRef 1 - Company name, contact details, contract value\nChatham House\nLisa O\u2019Daly \u2013 Managing Director\nlodaly@chathamhouse.org\n\u00a3560,000\nRef 2 - Company name, contact details, contract value\nThe Knightsbridge\nChris Barrass \u2013 Managing Director\nchris.barrass@theknightsbridge.com\n\u00a31,100,000 Ref 3 - Company name, contact details, contract value\nSean Donnelly\nHead of Procurement\nIVC\nsean.donnelly@ivcevidensia.com\n\u00a37,000,000\nSECTION C: INSURANCE\nPlease provide details of all insurance cover currently in force. If you reach and are successful at the tender stage, adequate insurance cover will be required. C1. Please insert copy documents of your organisation\u2019s insurance cover in respect of employer\u2019s liability, public liability, and any other relevant policies (including details of Fidelity & PI cover). Please summarise these below. Policy Insurer Indemnity Limit (\u00a3)\nPublic and Products Liability\nGallagher\n\u00a310,000,000\nEmployers Liability\nGallagher\n\u00a310,000,000\nProfessional Indemnity\nGallagher\n\u00a32,000,000\nSECTION D: TECHNICAL CAPACITY AND RESOURCES\nD1. Please list your Top 3 Clients by Contract Value for similar contracts that your organisation has carried out within the last 3 years.\nClients Name\nScope of the Services\nTotal Value of the Contract\nContract Duration\nIVC\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a37,000,000\n3+2years\nStonegate\nProjects and Reactive Support\n\u00a32,000,000\n2 years\nThe Knightsbridge\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a31,100,000\n3+2 years\nD2. Please list your Employees Structure & Nos. for that your organisation has employed for each of the last 3 years. Category 2023 2022 2021 Managers / Supervisors\n5\n2\n2 Operatives\n7\n2\n1 Apprentices\n1\n1\n0 Administrative Staff\n2\n1\n1\nD3. Please describe your organisation\u2019s approach to initial staff training in relation to the buildings they will be maintaining on this contract (1000 words max)\nAll our supply chain partners are fully inducted and trained before they can be on-boarded with IEM.\nWe have a thorough partner on-boarding process that we are happy to share if required, as a high-level overview:\n\u2022\nIEM has a dedicated Supply Chain Manager who ensures all our partners are fully onboarded, have gone through the IEM induction process then trained.\n\u2022\nA PQQ is always carried out, then we will meet with all new partners.\n\u2022\nDuring the induction process we ensure our partners are aware of our culture, values and service levels, as well as SLA\u2019s and individual customer expectations (as SLA\u2019s and prioritisation levels can vary from client-to-client)\n\u2022\nAll our partners must also be safe contractor trained and accredited before they are able to work with any of our customers.\n\u2022\nAfter initial on-boarding we also have a sign off period, this process is carried out by our Operations Manager, Technical Manager and Supply Chain Manager\n\u2022\nAll partners have to be trained in our AIMS system.\n\u2022\nAll insurance and certifications are checked, these have to be correct and live for contractors to be able to work with IEM, our AIMS system will send us reminders as to when these are due to expire so that we can monitor.\n\u2022\nFull Health & Safety checks are carried out.\n\u2022\nRegular Performance reviews are scheduled from the outset.\nAlong with partner onboarding internal staff go through a thorough induction, which focuses on IEM ethos, system training (with trade tests throughout the initial 3 weeks process and further scheduled throughout the year), and customer service training.\nWe are happy to share the internal induction precis if required.\nD3.1 Please describe your organisation\u2019s approach to the control and management of specialist sub-contractors 
  (1000 words max).\nSome of the information is covered above, however, some of the main points are as follows:\n\u2022\nWe have a dedicated supply chain manager that manages all our sub-contractors, both in relation to onboarding but then also from a continuous improvement perspective\n\u2022\nWith more than 1500 contractors and sub-contractors that work with us, all hard FM disciplines are covered, so we have to be very diligent in relation to their control and management.\n\u2022\nAt the outset we will have a formalised partnership agreement that is agreed by both IEM and sub-contractor, this includes the non-negotiable of everyone that works with IEM being Alcumus Safe Contractor accredited.\n\u2022\nWe have very clear terms and SLA\u2019s, which we are happy to share, and these are in place when our contractors start having conversations with us.\n\u2022\nAfter on-boarding and an initial probation period is completed, the sub-contractors are signed off and performance reviews are put in place which are then carried out by our supply chain manager.\n\u2022\nPart of our continuous improvement and monitoring process includes regular feedback documents being sent to our customers in relation to all our partners, we then share this during all our performance reviews.\nD4. What mechanisms do you have in place to ensure that you maintain high standards for the provision of MEBF maintenance within the built environment. (1000 words max).\nWe continually seek continual improvement to ensure our service delivery remains to a high standard, this includes.\n\u2022\nCompliance with Regulations: we ensure strict adherence to statutory compliance and legal compliances using CIBSE Guide M as an example, and safety standards.\n\u2022\nQuality Management Systems (QMS): Implementing and maintaining QMS standards such as ISO 9001 helps establish and follow processes that ensure high-quality service delivery.\n\u2022\nSkilled Workforce: Ensuring that contractor partner's maintenance teams are well-trained, certified, and equipped with the necessary skills and knowledge to perform their duties effectively and safely.\n\u2022\nPreventive Maintenance Programs: Developing and implementing preventive maintenance schedules to address potential issues proactively, thus minimising disruptions and costly repairs.\n\u2022\nAsset Management: Implementing robust asset management systems to monitor the condition of equipment and facilities, plan for replacements or repairs, and maximize the lifespan of assets.\n\u2022\nTechnology Integration: Using advanced technologies, such as CAFAM Systems, to streamline maintenance processes, monitor work orders, and manage resources efficiently.\n\u2022\nContinuous Improvement: Establishing a culture of continuous improvement by regularly reviewing and updating processes based on feedback from clients and staff to enhance efficiency and effectiveness.\n\u2022\nEmergency Response Planning: Developing and regularly updating emergency response plans to handle unforeseen events or crises effectively, minimizing potential damage and downtime.\n\u2022\nSupplier and Contractor Management: Selecting reliable suppliers and contractors, setting clear expectations and performance criteria, and regularly assessing their performance.\n\u2022\nPerformance Metrics: Defining and measuring key performance indicators (KPIs) to assess the effectiveness of maintenance activities and identify areas for improvement.\n\u2022\nEnvironmental Sustainability: Integrating environmentally sustainable practices into maintenance activities to minimize the impact on the environment and promote long-term sustainability.\n\u2022\nClient Communication: Maintaining open and transparent communication with clients regarding maintenance activities, schedules, and any potential disruptions.\n\u2022\nTraining and Development: Providing ongoing training and development opportunities for staff to keep them updated on industry best practices and new technologies.\n\u2022\nRegular Audits and Inspections: Conducting regular audits and inspections to ensure that maintenance activities align with established standards and procedures.\n\u2022\nFeedback Mechanisms: Establishing mechanisms for collecting feedback from clients and stakeholders to continuously assess and improve service quality.\nD5. Please provide a summary of your procedures for contract Management and Quality Audit (1000 words max).\nIEM are fully Safe Contractor as well as Principal Safety Accredited, this includes annual audits on our processes, with Safe Contractor carrying out monthly automated assessments on areas such as insurances, H&S, financial and sustainability.\nWe use the Safe Contractor portal to carry out the base management of our supply chain partners.\nWe also carry out our quarterly assessment meeting with our supply chain partners, which covers the data gathered during task visits, cost management and response management, the spot site visit audits are also evaluated at these meetings.\nWe also have our internal annual ISO 9001, 14001 and 45001 audits.\nD6. Can you provide an example of how you have ensured that you provide an exceptional service to a customer with buildings in multiple locations. (500 words max).\nAlmost all our clients, apart from the highly prestigious Chatham House and Knightsbridge apartments are multi-site locations.\nSupporting multi-site locations is IEM\u2019s sweet spot. The quantity of contractors that we have, with the nationwide geographical spread, means we offer support across the whole of the UK.\nOur clients include IVC vets (1400 sites), Stonegate Pubs (4500 sites) Arnold Clark (250 sites) these are just a few examples.\nAs mentioned, we have full nationwide coverage (Inc Ireland) and within almost all geographical locations, we operate 3 tiers of contractors per discipline, this gives IEM more choices and supports us from an availability and pricing perspective.\nAt the initial on-boarding, our operational processes and rhythms are agreed, these are then carried out during the relationship.\nAs an example, one of our partners, that works with IEM on IVC fire and security disciplines, have the following ways of working (Others are very similar):\n\u2022\nA Monday Operational Call to go through all outstanding jobs.\n\u2022\nA deep dive into SLA\u2019s and delivery weekly\n\u2022\nA monthly more in-depth dive call\n\u2022\nA visit to partners site every quarter to go through the account in detail and discuss what is working and areas of improvement.\nD7. Please provide an overview of your company\u2019s approach to corporate social responsibility (CSR)? Please provide a list of six core operational aspects that your CSR policy considers. (1000 words max).\nIEM truly values itself in relation to corporate social responsibility and it is a key part of what makes us what we are, a few examples of these are below and these can be discussed if application is progressed:\n\u2022\nWe are NCZ accredited (Neutral Carbon Zone) This accreditation provides us with independent verification and is an internationally recognised accreditation showing that IEM is following the right processes and procedures to get us to net zero. This is renewed yearly. We are also now working to ensure a key part of our supply chain is also accredited.\n\u2022\nOur vision, mission and objectives were created by the whole team, is kept alive through various channels and before any new staff members can work with us, they must have done our induction which includes all of the above. This ensures alignment and continuity\n\u2022\nOur goals and objectives are created yearly with the full team\u2019s involvements, this includes setting objectives for the year ahead and reviewing previous years performance. What differentiates IEM, is that annual goal setting is completed at a full team meeting of all employees not just senior management.\n\u2022\nWe are very strong exponents of supporting the veteran military community through a variety of means.\no\nAmbassadors and prime sponsors of one of the UK\u2019s leading military charities Care After Combat\no\nFounder Alistair Scott is Director of IWFM audit and risk committee and jointly formed the IWFM \u201cVeteran\u2019s in FM\u201d Professional Networking Group..\n\u2022\nIEM are proud to be National Living Wage Accredited.\n\u2022\nWe and every one of our contractors are Safe Contractor accredited.\nSECTION E: QUALITY AND STANDARDS\nE1. Please insert details (list) of the quality assurance certification that your company holds e.g., BS EN ISO9001, ISO14001, CHAS, IIP or equivalents. Please provide copies of certificates in a separate file.\n\u2022\nISO9001\n\u2022\nISO14001\n\u2022\nISO45001\n\u2022\nSafe Contractor\n\u2022\nPrincipal Safety\nE2. Please provide details of any memberships of trade associations and other relevant accreditations. Please provide copies of certificates in a separate file.\n\u2022\nBESA Associate\n\u2022\nIWFM\n\u2022\nIET\nSECTION F: HEALTH AND SAFETY\nMandatory to be selected to Invitation to Tender. Yes No F1.1 The Supplier must have a written Health and Safety at Work policy? Please note that this document must not be more than 12-months-old.\nYes\nF1.2 Please provide brief details how your Health & Safety Policy is communicated to your staff and the systems and procedures you have in place for monitoring, reviewing, and reporting of Health and Safety issues. (1000 words max).\nThis is covered in depth during our various ISO accreditation process, but a few of the key points are as followed:\n\u2022\nWe have a separate Health and Safety committee, represented by a variety of team members not just senior management.\n\u2022\nAll minutes and actions are documented, with clear next steps.\n\u2022\nThis meeting is held monthly and an external H+S representative attends and is also accountable for training.\n\u2022\nH+S is a key part of our induction process.\n\u2022\nAll minutes and next steps are always on out staff communication board.\n\u2022\nAny Health and Safety issues are reported through the H+S internal and external rep, these are actioned and recorded, they are also covered at our H+S meeting as well as our normal monthly meeting.\nF1.3 H&S Policy Attached:\nYes\nF1.4 Does your organisation have any Health & Safety Accreditation, e.g., ISO 18001 or equivalent?\nSafe Contractor\nPrincipal Safety\nISO:9001\nF1.5 If \u201cYes,\u201d please provide copies of any relevant certificates as separate attachments\nF3. Please detail any HSE / local authority enforcing action taken against your company in the last three\nyears (up to 500 words per incident):\nN/A\nF4. Please include details any RIDDOR reportable accidents by your company within the last three years.\nN/A\nSECTION G. EQUALITY & DIVERSITY\nYour company will be evaluated for equality and diversity in employment based on your answers to these questions. Please ensure that you answer them all.\nPlease provide sufficient information to enable OC to make a fair and accurate assessment of how, as an employer and/or service provider, you have dealt with equality issues.\nMandatory to be selected to Invitation to Tender. Yes No G1. The Supplier must have a written Equalities & Diversity Policy? Please note that this document must not be more than 12 months old.\nYES\nG2. Equalities & Diversity Policy Attached:\nG3. Is it your Company policy as an employer to comply with your statutory obligations under the Equality Act 2010 (or European equivalents), and accordingly your practice not to treat one group less favourably than others?\nYES\nG4. Please provide details of the Right to Work in UK \u2013 Visa Checks you operate? (1000 words max).\nThe Right to work is assessed during the interview stage, the preferred process is to check the applicant's right to work using the online portal (this requires the applicant to share their code).\nIf this isn\u2019t possible, we use our employment partner who assesses the right to work using the applicant's documents and Identity Document Validation Technology (IDVT).\nSECTION H: DECLARATION\nH1: Declaration Name, Position & Signature Date We confirm and declare that the contents of this RFI submission and all details stated above are true and correct.\nAlistair Scott\nFounder\n16th Nov 2023"
   
  Registered office (if different from above).\nOffice 5, Boleyn Suite,\nHever Road,\nEdenbridge\nKent,\nTN8 7NP\nA5. Are you or is your organisation a: Sole Trader?\nPartnership?\nPrivate Limited Company?\nYes Public limited Company?\nRegistered Charity?\nOther?\nPlease Specify?\nA6. Limited Companies Please state the companies date of incorporation and registration number under the Companies Act 1985. OR\nDate\n02/11/2018\nRegistration Number\n11657337\nDate of registration and the company's registration number under the Industrial and Provident Societies Acts 1965 to 1978. OR\nDate\nNumber\nPartnerships Please state the date the partnership was formed, began trading and Total number of partners. Are the partnerships being a member of a group? If \u201cYes,\u201d detail other relationships within the group and comment on the group structure. OR\nDate\nNumber\nTotal Number of Partners\nAdditional Comments\nSole Trader\nDate\nDate when Supplier began trading\nA7. If the Supplier is a member of a group of companies or subsidiary of another company as defined by Section 736 (1) of the Companies Act 1985, give the names and company numbers of the holding company and any companies in-between you and the holding company, clearly stating the relationship with your organisation.\nCompany Name\nCompany Number\nRelationship\nN/A\nA8. Is the parent company or ultimate holding company prepared to guarantee the performance of the Supplier?\nYes:\nNo:\nN/A\nIf yes, please provide: Name of Company\nRegistration number\nRelationship with your company\nA9. What is your organisation\u2019s VAT number?\n310404272\nSECTION B: FINANCIAL INFORMATION & REFERENCE INFORMATION\nB1 Name of Bankers:\nSantander Address of Bankers:\n2 Triton Square,\nRegents Place\nLondon,\nNW1 3AN Name of Auditors:\nN/A\nB2. Please provide details of the past three years turnover of the company Year Ending 2019 - 20\n\u00a3122,000\nYear Ending 2020 - 21\n\u00a3681,000\nYear Ending 2021 - 22\n\u00a31,174,000\nB3. Please provide details of three existing customers with similar contracts that we can contact for references.\nRef 1 - Company name, contact details, contract value\nChatham House\nLisa O\u2019Daly \u2013 Managing Director\nlodaly@chathamhouse.org\n\u00a3560,000\nRef 2 - Company name, contact details, contract value\nThe Knightsbridge\nChris Barrass \u2013 Managing Director\nchris.barrass@theknightsbridge.com\n\u00a31,100,000 Ref 3 - Company name, contact details, contract value\nSean Donnelly\nHead of Procurement\nIVC\nsean.donnelly@ivcevidensia.com\n\u00a37,000,000\nSECTION C: INSURANCE\nPlease provide details of all insurance cover currently in force. If you reach and are successful at the tender stage, adequate insurance cover will be required. C1. Please insert copy documents of your organisation\u2019s insurance cover in respect of employer\u2019s liability, public liability, and any other relevant policies (including details of Fidelity & PI cover). Please summarise these below. Policy Insurer Indemnity Limit (\u00a3)\nPublic and Products Liability\nGallagher\n\u00a310,000,000\nEmployers Liability\nGallagher\n\u00a310,000,000\nProfessional Indemnity\nGallagher\n\u00a32,000,000\nSECTION D: TECHNICAL CAPACITY AND RESOURCES\nD1. Please list your Top 3 Clients by Contract Value for similar contracts that your organisation has carried out within the last 3 years.\nClients Name\nScope of the Services\nTotal Value of the Contract\nContract Duration\nIVC\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a37,000,000\n3+2years\nStonegate\nProjects and Reactive Support\n\u00a32,000,000\n2 years\nThe Knightsbridge\nFull FM Integrator Package (PPM, Remedial, Reactive maintenance and Projects)\n\u00a31,100,000\n3+2 years\nD2. Please list your Employees Structure & Nos. for that your organisation has employed for each of the last 3 years. Category 2023 2022 2021 Managers / Supervisors\n5\n2\n2 Operatives\n7\n2\n1 Apprentices\n1\n1\n0 Administrative Staff\n2\n1\n1\nD3. Please describe your organisation\u2019s approach to initial staff training in relation to the buildings they will be maintaining on this contract (1000 words max)\nAll our supply chain partners are fully inducted and trained before they can be on-boarded with IEM.\nWe have a thorough partner on-boarding process that we are happy to share if required, as a high-level overview:\n\u2022\nIEM has a dedicated Supply Chain Manager who ensures all our partners are fully onboarded, have gone through the IEM induction process then trained.\n\u2022\nA PQQ is always carried out, then we will meet with all new partners.\n\u2022\nDuring the induction process we ensure our partners are aware of our culture, values and service levels, as well as SLA\u2019s and individual customer expectations (as SLA\u2019s and prioritisation levels can vary from client-to-client)\n\u2022\nAll our partners must also be safe contractor trained and accredited before they are able to work with any of our customers.\n\u2022\nAfter initial on-boarding we also have a sign off period, this process is carried out by our Operations Manager, Technical Manager and Supply Chain Manager\n\u2022\nAll partners have to be trained in our AIMS system.\n\u2022\nAll insurance and certifications are checked, these have to be correct and live for contractors to be able to work with IEM, our AIMS system will send us reminders as to when these are due to expire so that we can monitor.\n\u2022\nFull Health & Safety checks are carried out.\n\u2022\nRegular Performance reviews are scheduled from the outset.\nAlong with partner onboarding internal staff go through a thorough induction, which focuses on IEM ethos, system training (with trade tests throughout the initial 3 weeks process and further scheduled throughout the year), and customer service training.\nWe are happy to share the internal induction precis if required.\nD3.1 Please describe your organisation\u2019s approach to the control and management of specialist sub-contractors (1000 words max).\nSome of the information is covered above, however, some of the main points are as follows:\n\u2022\nWe have a dedicated supply chain manager that manages all our sub-contractors, both in relation to onboarding but then also from a continuous improvement perspective\n\u2022\nWith more than 1500 contractors and sub-contractors that work with us, all hard FM disciplines are covered, so we have to be very diligent in relation to their control and management.\n\u2022\nAt the outset we will have a formalised partnership agreement that is agreed by both IEM and sub-contractor, 
  this includes the non-negotiable of everyone that works with IEM being Alcumus Safe Contractor accredited.\n\u2022\nWe have very clear terms and SLA\u2019s, which we are happy to share, and these are in place when our contractors start having conversations with us.\n\u2022\nAfter on-boarding and an initial probation period is completed, the sub-contractors are signed off and performance reviews are put in place which are then carried out by our supply chain manager.\n\u2022\nPart of our continuous improvement and monitoring process includes regular feedback documents being sent to our customers in relation to all our partners, we then share this during all our performance reviews.\nD4. What mechanisms do you have in place to ensure that you maintain high standards for the provision of MEBF maintenance within the built environment. (1000 words max).\nWe continually seek continual improvement to ensure our service delivery remains to a high standard, this includes.\n\u2022\nCompliance with Regulations: we ensure strict adherence to statutory compliance and legal compliances using CIBSE Guide M as an example, and safety standards.\n\u2022\nQuality Management Systems (QMS): Implementing and maintaining QMS standards such as ISO 9001 helps establish and follow processes that ensure high-quality service delivery.\n\u2022\nSkilled Workforce: Ensuring that contractor partner's maintenance teams are well-trained, certified, and equipped with the necessary skills and knowledge to perform their duties effectively and safely.\n\u2022\nPreventive Maintenance Programs: Developing and implementing preventive maintenance schedules to address potential issues proactively, thus minimising disruptions and costly repairs.\n\u2022\nAsset Management: Implementing robust asset management systems to monitor the condition of equipment and facilities, plan for replacements or repairs, and maximize the lifespan of assets.\n\u2022\nTechnology Integration: Using advanced technologies, such as CAFAM Systems, to streamline maintenance processes, monitor work orders, and manage resources efficiently.\n\u2022\nContinuous Improvement: Establishing a culture of continuous improvement by regularly reviewing and updating processes based on feedback from clients and staff to enhance efficiency and effectiveness.\n\u2022\nEmergency Response Planning: Developing and regularly updating emergency response plans to handle unforeseen events or crises effectively, minimizing potential damage and downtime.\n\u2022\nSupplier and Contractor Management: Selecting reliable suppliers and contractors, setting clear expectations and performance criteria, and regularly assessing their performance.\n\u2022\nPerformance Metrics: Defining and measuring key performance indicators (KPIs) to assess the effectiveness of maintenance activities and identify areas for improvement.\n\u2022\nEnvironmental Sustainability: Integrating environmentally sustainable practices into maintenance activities to minimize the impact on the environment and promote long-term sustainability.\n\u2022\nClient Communication: Maintaining open and transparent communication with clients regarding maintenance activities, schedules, and any potential disruptions.\n\u2022\nTraining and Development: Providing ongoing training and development opportunities for staff to keep them updated on industry best practices and new technologies.\n\u2022\nRegular Audits and Inspections: Conducting regular audits and inspections to ensure that maintenance activities align with established standards and procedures.\n\u2022\nFeedback Mechanisms: Establishing mechanisms for collecting feedback from clients and stakeholders to continuously assess and improve service quality.\nD5. Please provide a summary of your procedures for contract Management and Quality Audit (1000 words max).\nIEM are fully Safe Contractor as well as Principal Safety Accredited, this includes annual audits on our processes, with Safe Contractor carrying out monthly automated assessments on areas such as insurances, H&S, financial and sustainability.\nWe use the Safe Contractor portal to carry out the base management of our supply chain partners.\nWe also carry out our quarterly assessment meeting with our supply chain partners, which covers the data gathered during task visits, cost management and response management, the spot site visit audits are also evaluated at these meetings.\nWe also have our internal annual ISO 9001, 14001 and 45001 audits.\nD6. Can you provide an example of how you have ensured that you provide an exceptional service to a customer with buildings in multiple locations. (500 words max).\nAlmost all our clients, apart from the highly prestigious Chatham House and Knightsbridge apartments are multi-site locations.\nSupporting multi-site locations is IEM\u2019s sweet spot. The quantity of contractors that we have, with the nationwide geographical spread, means we offer support across the whole of the UK.\nOur clients include IVC vets (1400 sites), Stonegate Pubs (4500 sites) Arnold Clark (250 sites) these are just a few examples.\nAs mentioned, we have full nationwide coverage (Inc Ireland) and within almost all geographical locations, we operate 3 tiers of contractors per discipline, this gives IEM more choices and supports us from an availability and pricing perspective.\nAt the initial on-boarding, our operational processes and rhythms are agreed, these are then carried out during the relationship.\nAs an example, one of our partners, that works with IEM on IVC fire and security disciplines, have the following ways of working (Others are very similar):\n\u2022\nA Monday Operational Call to go through all outstanding jobs.\n\u2022\nA deep dive into SLA\u2019s and delivery weekly\n\u2022\nA monthly more in-depth dive call\n\u2022\nA visit to partners site every quarter to go through the account in detail and discuss what is working and areas of improvement.\nD7. Please provide an overview of your company\u2019s approach to corporate social responsibility (CSR)? Please provide a list of six core operational aspects that your CSR policy considers. (1000 words max).\nIEM truly values itself in relation to corporate social responsibility and it is a key part of what makes us what we are, a few examples of these are below and these can be discussed if application is progressed:\n\u2022\nWe are NCZ accredited (Neutral Carbon Zone) This accreditation provides us with independent verification and is an internationally recognised accreditation showing that IEM is following the right processes and procedures to get us to net zero. This is renewed yearly. We are also now working to ensure a key part of our supply chain is also accredited.\n\u2022\nOur vision, mission and objectives were created by the whole team, is kept alive through various 
  channels and before any new staff members can work with us, they must have done our induction which includes all of the above. This ensures alignment and continuity\n\u2022\nOur goals and objectives are created yearly with the full team\u2019s involvements, this includes setting objectives for the year ahead and reviewing previous years performance. What differentiates IEM, is that annual goal setting is completed at a full team meeting of all employees not just senior management.\n\u2022\nWe are very strong exponents of supporting the veteran military community through a variety of means.\no\nAmbassadors and prime sponsors of one of the UK\u2019s leading military charities Care After Combat\no\nFounder Alistair Scott is Director of IWFM audit and risk committee and jointly formed the IWFM \u201cVeteran\u2019s in FM\u201d Professional Networking Group..\n\u2022\nIEM are proud to be National Living Wage Accredited.\n\u2022\nWe and every one of our contractors are Safe Contractor accredited.\nSECTION E: QUALITY AND STANDARDS\nE1. Please insert details (list) of the quality assurance certification that your company holds e.g., BS EN ISO9001, ISO14001, CHAS, IIP or equivalents. Please provide copies of certificates in a separate file.\n\u2022\nISO9001\n\u2022\nISO14001\n\u2022\nISO45001\n\u2022\nSafe Contractor\n\u2022\nPrincipal Safety\nE2. Please provide details of any memberships of trade associations and other relevant accreditations. Please provide copies of certificates in a separate file.\n\u2022\nBESA Associate\n\u2022\nIWFM\n\u2022\nIET\nSECTION F: HEALTH AND SAFETY\nMandatory to be selected to Invitation to Tender. Yes No F1.1 The Supplier must have a written Health and Safety at Work policy? Please note that this document must not be more than 12-months-old.\nYes\nF1.2 Please provide brief details how your Health & Safety Policy is communicated to your staff and the systems and procedures you have in place for monitoring, reviewing, and reporting of Health and Safety issues. (1000 words max).\nThis is covered in depth during our various ISO accreditation process, but a few of the key points are as followed:\n\u2022\nWe have a separate Health and Safety committee, represented by a variety of team members not just senior management.\n\u2022\nAll minutes and actions are documented, with clear next steps.\n\u2022\nThis meeting is held monthly and an external H+S representative attends and is also accountable for training.\n\u2022\nH+S is a key part of our induction process.\n\u2022\nAll minutes and next steps are always on out staff communication board.\n\u2022\nAny Health and Safety issues are reported through the H+S internal and external rep, these are actioned and recorded, they are also covered at our H+S meeting as well as our normal monthly meeting.\nF1.3 H&S Policy Attached:\nYes\nF1.4 Does your organisation have any Health & Safety Accreditation, e.g., ISO 18001 or equivalent?\nSafe Contractor\nPrincipal Safety\nISO:9001\nF1.5 If \u201cYes,\u201d please provide copies of any relevant certificates as separate attachments\nF3. Please detail any HSE / local authority enforcing action taken against your company in the last three\nyears (up to 500 words per incident):\nN/A\nF4. Please include details any RIDDOR reportable accidents by your company within the last three years.\nN/A\nSECTION G. EQUALITY & DIVERSITY\nYour company will be evaluated for equality and diversity in employment based on your answers to these questions. Please ensure that you answer them all.\nPlease provide sufficient information to enable OC to make a fair and accurate assessment of how, as an employer and/or service provider, you have dealt with equality issues.\nMandatory to be selected to Invitation to Tender. Yes No G1. The Supplier must have a written Equalities & Diversity Policy? Please note that this document must not be more than 12 months old.\nYES\nG2. Equalities & Diversity Policy Attached:\nG3. Is it your Company policy as an employer to comply with your statutory obligations under the Equality Act 2010 (or European equivalents), and accordingly your practice not to treat one group less favourably than others?\nYES\nG4. Please provide details of the Right to Work in UK \u2013 Visa Checks you operate? (1000 words max).\nThe Right to work is assessed during the interview stage, the preferred process is to check the applicant's right to work using the online portal (this requires the applicant to share their code).\nIf this isn\u2019t possible, we use our employment partner who assesses the right to work using the applicant's documents and Identity Document Validation Technology (IDVT).\nSECTION H: DECLARATION\nH1: Declaration Name, Position & Signature Date We confirm and declare that the contents of this RFI submission and all details stated above are true and correct.\nAlistair Scott\nFounder\n16th Nov 2023


  Good dental care really matters. We provide dental care for 1.5 million patients every year across the UK and Ireland. Today, we support over 370 practices, partner with more than 2,400 clinicians and empower more than 4,500 practice colleagues \u2013 to enable better health and happiness across lifetimes.  Our practices are integral parts of their local communities, and we support our clinicians and practice teams to deliver the best care possible for their patients, every day.  We know that every patient and every community is unique.  As a dental group we strive to balance celebrating the individuality of our clinicians and practices, with using the benefits of our scale and commitment to deliver excellent dental care.  We\u2019re also part of the wider Portman Healthcare International Group which has a presence in five European countries.\n1.2\tProject Context, Background and Strategic Objectives".

  Following the merger of Portman Dental Care and Dentex Health in 2023, we now operate as PortmanDentex.  The recently combined business forms one of the largest dental groups in the UK with plans to continue our exciting growth.  \n1.2.2\tNow operating as one business, a review of PortmanDentex\u2019s ways of working has been undertaken with a view to taking the best elements of each legacy business, whilst improving and optimising our set up, given our larger scale.  \n1.2.3\tAs we have brought the two legacy businesses together, it has heightened the need for the business to review the approach as to how we manage our estate,  how we provide exceptional service and maintain standards to our practices and practice based colleagues, how we procure property services and, ultimately, how we manage our growing estate in a more efficient and strategic manner.   \n1.2.4\tMaintenance services today are delivered across the estate in a broadly decentralised manner.  Practice Managers are accountable for their individual practice P&Ls and in many instances will determine when, how and who carries out their maintenance, particularly from a non-urgent reactive maintenance perspective.  As a result, contractors are not routinely managed from a relationship or standards perspective.  \n1.2.5\tA reactive maintenance framework was put in place by the legacy Portman Property and Procurement team in 2020, although this is not widely used, managed or enforced today.  Legacy Dentex practices have historically always used their own locally procured contractors for reactive and planned maintenance.

  Due to PortmanDentex\u2019s rapid growth via M&A over the past five years and our strategic objectives to manage FM in a more holistic manner, the contractors that were selected on the 2020 framework are no longer the right partners for our future aspirations.  \n1.2.7\tPlanned Maintenance, generally statutory property compliance testing and risk assessments, for the legacy Portman estate are coordinated centrally by PortmanDentex\u2019s in-house Safety and Quality (S&Q) team with any remedial works required being managed by the PortmanDentex in-house Property team.  \n1.2.8\tLegacy Dentex sites have historically been locally managed and coordinated by each site and as such, visibility of remedial work undertaken following risk assessments and statutory property compliance testing is less documented.  For risk assessments, we are now inspecting the legacy Dentex estate in the same format as the Portman one and so we anticipate more remedial activity for legacy Dentex sites during 2026 onwards, following risk assessments and compliance testing carried out during 2025.  \n1.2.9\tRemedial works are tendered by the Property team with support from our current property consultancy supplier, Border Consultancy.  Payment is made once new certification has been provided.  \n1.2.10\tPlanned Project Work (typically > \u00a35k) is managed centrally by the Property team and is generally driven by requirements from Operations; project work following acquisitions; mergers and/or relocation of practices and fabric PPMs.  \n1.2.11\tThere is no central helpdesk, no CAFM system and minimal formal knowledge management processes in place.   A business wide ticketing system is used in some instances, however this is not fit for purpose, is not used consistently across the estate and does not record project work or store key estate information.  A lot of knowledge is held in colleague\u2019s emails, locally stored files and in colleague\u2019s heads.\n1.2.12\tThe overarching strategic objectives for PortmanDentex\u2019s future FM solution are:  \n\u2022\tTo establish a new operating model that provides greater efficiency, transparency and visibility for the Property function \u2013 bringing ownership to all matters relating to the physical estate to the Property team.  This will deliver efficiency, create simplicity and consistency.  \n\u2022\tTo select an expert Service Provider who PortmanDentex can partner with to deliver the requirements of PortmanDentex.  \n\u2022\tTo improve service quality and internal customer focus.  \n\u2022\tTo introduce greater innovation and use of technology.  \n\u2022\tTo improve knowledge management across the estate and to have a \u2018single point of truth\u2019 for all matters regarding the entire estate.  \n\u2022\tTo implement greater spend control and visibility to enable significantly improved budgeting and future life cycle planning.  \n\u2022\tTo deliver significant cost savings to enable us to re-invest in our estate and future growth.  \n\u2022\tTo consolidate and drive value from the large, fragmented supply chain.

  Cost Saving and Cost Control \u2013 the new solution will deliver significant commercial benefit to PortmanDentex and will realise real cost savings that will hit the bottom line.  The ability to flex service and manage costs according to budgets and/or trading performance is vital.  \n\u2022\tService Delivery \u2013 the new solution must deliver the standard of service that is synonymous with PortmanDentex and provide an appropriate service to the PortmanDentex stakeholders.  \n1.2.14\tIn responding to this RFP, the Bidder should note that PortmanDentex welcomes any proposals for service improvement which offer competitive commercial terms.  All proposals must clearly explain their benefits to PortmanDentex and the impact on the overall service.\n1.3\tBusiness Requirements
  PortmanDentex\u2019s  business requirements for the successful delivery of maintenance are as follows:\n\u2022\tTo support PortmanDentex colleagues with providing an appropriate service to its practices through an effective and efficient maintenance operation.\n\u2022\tTo provide safe, clean, legally compliant clinical and comfortable environments for our patients and colleagues. \n\u2022\tImplement robust systems for monitoring and reporting H&S and contractor performance.  \n\u2022\tOptimising the life span of our buildings, plant and equipment, enabling colleagues and clinicians to carry out their business functions effectively.  \n\u2022\tUnderstanding the maintenance needs of PortmanDentex and provide services that support PortmanDentex to achieve its aims and objectives.  \n\u2022\tEfficiently manage the use of resources to deliver activities when they are required at the lowest cost achievable for the appropriate quality of service required. \n\u2022\tProvide PortmanDentex with a value for money service by being transparent about costs, priorities, service levels, performance and the added value FM delivers to the business. Value for money will also be achieved by taking a more commercial approach and having an awareness of the need for efficiency, cost-effectiveness as well as customer care.\n\u2022\tResponsive to change by putting in place an operating model that better adapts to an ever-changing healthcare environment.\n\u2022\tUphold the principles and culture of PortmanDentex by communicating and building trusted relationships with its patients and suppliers fostering a culture of mutual respect, courtesy and equality.

  The procurement timeline is summarised in Table 2.1\n2.1.2\tPlease note that should the deadlines need to be modified; this will be communicated to the Bidders via email.  If any of the dates in the procurement timeline are not achievable, the Bidder shall inform PortmanDentex at the earliest opportunity.
  All deadlines are 5pm on the specified due date (unless otherwise stated), with the exception of dialogue meetings and final presentations.\nTable 2.1\nAction / Key Milestone\tDue Date\nLaunch RFP\t11-Nov-24\nBidders confirm intention to Bid / No Bid\t18-Nov-24\nDeadline for Bidder to submit questions\t13-Dec-24\nDeadline for PD response to Bidder questions\t20-Dec-24\nDialogue Meeting #1 - London\t09-Dec-2024\n12-Dec-2024\nDialogue Meeting # 2 - Cheltenham\t16-Jan-2025\n17-Jan-2025\nDeadline for RFP response submission \t24-Jan-25\nBidder final presentations - London\t10-Feb-2025\n11-Feb-2025\nAppoint preferred Bidder / Inform unsuccessful Bidders*\t03-Mar-25\nFinal Contract Negotiation / Due Diligence with Preferred Bidder*\t14-Mar-25\nPD Approval to Sign Contract\t21-Mar-25\nContract Signatures*\t24-Mar-25\nMobilisation Commences*\t31-Mar-25\nContract Go-Live (assuming 3 month mobilisation period TBC)*\t01-Jul-25\n     *estimated\n2.2\tBidder questions
  
Bidders will have the opportunity to ask questions, subject to the timings set out above. All questions must be submitted in writing via email using the template provided in PortmanDentexFMTender - Appendix 9 - Bidder Question Template. \n2.2.1.2\tIn order to manage the administration of the question/answer process throughout the RFP, Bidders are requested to ask questions once a week on Tuesday before 17:00.  PortmanDentex will issue answers once a week on Friday by 17:00.  PortmanDentex will endeavour to respond to questions in a timely manner.  \n2.2.1.3\tPortmanDentex\u2019s responses to the questions shall be circulated to all Bidders where the content is not confidential to any one party, in an anonymous format so the source of the question will not be disclosed.\n2.2.1.4\tPortmanDentex reserves the right, at its sole discretion, not to respond to any of the questions by Bidders.  For avoidance of doubt, PortmanDentex will aim to address all questions and explain relevant reason(s) for questions to which no response is provided.\n2.3\tTender Portal SharePoint Site

PortmanDentex have a dedicated SharePoint site for Bidders to download tender documentation, upon confirmation of their intention to bid and confirmation of the person who should access the SharePoint site.  \n2.3.1.2\tBidders are required to upload their RFP response documentation to the PortmanDentex Tender Portal SharePoint site.  \n2.4\tBidder References
As part of the response to this RFP, Bidders are requested to provide two customer references that are relevant to the services requested in this RFP and that are currently being provided by the Bidder.  PortmanDentex reserves the right to contact the referees listed to arrange site visits and/or reference meetings / calls.\n2.5\tDialogue Meetings
The Dialogue meetings shall take place at either our London or Cheltenham offices (unless otherwise stated).  Bidders will receive full details related to meeting content and logistics closer to the dates.  Detailed agendas, discussion points and a list of PortmanDentex attendees will be released in advance of the meetings.  Sessions are expected to cover commercial, technical, service, people and legal aspects of the project.  \n2.6\tBidder Final Presentations
The Bidder final presentations shall take place at PortmanDentex London Head Office.  As an indication, the final presentations are expected to be 2 hour time slots including a presentation and Q&A session.  \n2.7\tCommunication Plan
All communication relating to this RFP, including the RFP response submission, shall be addressed to:\n2.7.1.2\tAdam Hillier, Head of Procurement and Hope Armstrong, Procurement Specialist (via email). adam.hillier@portmandental.co.uk ; hope.armstrong@portmandental.co.uk \n2.7.1.3\tIf any urgent communications are required (e.g. expecting to be late for a meeting) please contact Adam Hillier on 07584 677 292.\n2.7.1.4\tAny questions regarding this RFP must be submitted in writing via email as per the instructions in Section 2.2.  Any questions submitted after the deadline in Table 2.1 of this RFP will not receive a response from PortmanDentex.\n2.8\tRFP General Terms

Information included in this proposal is proprietary and confidential regarding PortmanDentex.\n2.8.2\tThe submission, receipt, and review of RFP responses do not obligate PortmanDentex in any way.  This RFP is not an offer of Contract and is intended solely for information and review purposes.\n2.8.3\tPortmanDentex is not obliged to provide the reasons for successful and unsuccessful responses.\n2.8.4\tPortmanDentex is not liable for any costs incurred by the Bidder in the preparation and presentation of the RFP responses.\n2.8.5\tThe Bidder shall be bound by the submitted RFP proposal in all respects for a period of six months, beginning on the date of submission.\n2.8.6\tThe Bidder must not participate in any consultation, communication, arrangement or understanding with another Bidder regarding any element of this RFP.\n2.8.7\tPortmanDentex reserves the right to amend, modify or withdraw this RFP after issuance.  All such amendments will be communicated to the Bidders.\n2.8.8\tPortmanDentex reserves the right to exclude Bidders during the process if in the opinion of PortmanDentex the quality or price of the solution on offer will not meet requirements or is not competitive and to continue with the Bidder in the process is not likely to rectify the issue. \n2.8.9\tThe Bidder must notify PortmanDentex at the earliest opportunity of any significant changes to the bidders\u2019 structure, financial stability, service delivery model, including personnel and locations.\n2.8.10\tPortmanDentex cannot provide any guarantees or assurances of business until such time as a Contract is signed.  Any award will be provisional and subject to contract until a formal Contract is signed on behalf of PortmanDentex.  \n2.9\tIntention to Bid

Upon receipt of this RFP, Bidders shall email a clear Intention to Bid or No Bid by the deadline in Table 2.1 to Adam Hillier and Hope Armstrong via email, including the nominated person who shall be given access to the PortmanDentex Tender Portal SharePoint site.    \n2.9.1.1\tAppendices to this RFP will be made available to Bidders following their confirmation that they will be submitting a bid.  Bidders are required to provide one contact name and email address to Adam Hillier and Hope Armstrong alongside their written confirmation of their intention to bid.  This nominated person will then be provided access to the PortmanDentex Tender Portal SharePoint where all tender documentation can be accessed and downloaded.  \n2.9.2\tIf the Bidder does not confirm its Intention to Bid or No Bid by the deadline in Table 2.1, PortmanDentex may exclude the Bidder from this and future tenders.\n2.10\tStructure of the RFP Response

Bidders are required to submit a comprehensive proposal to meet PortmanDentex\u2019s requirements and satisfy all elements of this RFP by the deadline in Table 2.1.\n2.10.2\tThe responses to this RFP shall be provided in four separate volumes as detailed below.  Please ensure that the Bidder Questions found in PortmanDentexFMTender - Appendix 1 - Bidder Questions are all addressed and answered in your response.  \nVolume 1: Executive Summary\nHigh-level summary of the proposed delivery model, including:\n\u2022\tApproach to service delivery, highlighting key delivery model features.\n\u2022\tSchedule of key milestones during service mobilisation and transition.\n\u2022\tList of the top risks and associated mitigation plan.\n\u2022\tSummary of key commercial terms and pricing.\nVolume 2: Service, People and Technical Solution \nPlease complete the following documentation / provide responses to the following:\n\u2022\tService Delivery Plans for the specifications outlined below:\n\u2022\tPlanned Maintenance\n\u2022\tReactive Maintenance\n\u2022\tOn Request Services \n\u2022\tRemedial Works \n\u2022\tHelpdesk and CAFM System \n\u2022\tManagement (including Account Management) \n\u2022\tReporting / Management Information \n\u2022\tSuggested improvements and efficiencies to the Service and Technical Specifications in Section 3 of this RFP Document, including the Service Levels set out in PortmanDentexFMTender - Appendix 10 - SLAs and KPIs.\n\u2022\tFor the Service and Technical Specifications, this must be done via mark-up using \u201cTrack Changes\u201d in Microsoft Word with associated commentary as to why suggested changes have been made.  Please send a marked-up Service Specification as part of your response to this RFP.\n\u2022\tFor the Service Levels and KPIs, please highlight any suggested changes or improvements in a marked up Excel document.  \n\u2022\tA detailed mobilisation plan including dates and activities including who is responsible for which activity
Commercial Terms & Pricing\nPlease complete the following documentation:\n\u2022\tPortmanDentexFMTender - Appendix 2 - Pricing Template


Contractual Information\nPlease review the following documentation:\n\u2022\tServices Contract Terms & Conditions based on PortmanDentexFMTender - Appendix 3 - Draft Contract and confirm acceptance of the Contract / principles and provide a mark-up using \u201cTrack Changes\u201d in Microsoft Word for any proposed changes.
The RFP responses shall be concise, well-indexed in an easy-to-follow format, and in sufficient detail to enable PortmanDentex to assess the overall approach.  Each page shall be numbered and include the Bidder\u2019s company name as a footer. \n2.10.4\tEnsure all files follow a consistent naming convention in the following format:  \nBidderName_VolumeRef_Title  \nExample:  DentalFM_Vol1_ExecSummary.pdf   \n2.10.5\tThe RFP responses shall form part of the basis of the Contract between PortmanDentex and the Service Provider, subject to a detailed discussion and negotiation.\n2.10.6\tAs the successful RFP response will form a key part of the basis of the Contract, PortmanDentex requests that the solutions proposed by Bidders are stated unambiguously.\n2.10.7\tFiles must be in Microsoft Word, PDF and/or Microsoft Excel.  They must be virus-free and not write-protected to aid PortmanDentex during review and analysis.

Traning :
Dealing with Challenging People / Situations" CPD-accredited course, earning 6 hours of CPD on November 14, 2024. 🌟

This experience has enhanced my ability to navigate complex interactions and tackle challenges with confidence and professionalism.
A big thank you to Integrated Estate Management Ltd for providing this incredible learning opportunity and valuable insights! 🙏..

the Consistently Delivering Exceptional Service course with Hamilton Mercer, accredited by the CPD Standards Office. 🎉
A big thank you to IEM for the opportunity and support. This course has enriched my understanding of customer service excellence, equating to 6 hours of CPD. I am looking forward to applying these skills in future endeavors! 🚀

COMPANY BACKGROUND
 Q: Provide a description of your company’s 
history, culture and capability in relation to 
Facilities Management.
 In your answer include relevant facts and figures e.g. annual 
revenues, growth in employee numbers, key customers, 
sector experience, year established, ownership structure, 
geographical coverage (UK and ROI?) etc.
 A: At IEM, we are driven by a singular mission: to simplify 
the complexities of estate management, which is centred 
around taking away the daily pain of managing your 
facilities, IEM is not just another service provider—we’re 
your partners in building efficient and thriving estates.
 We operate to 3 principles,
 Our People come first.
 Our Partners are precious.
 We are the leaders on Building Compliance.
 Founded in the early days of Covid 2020 by Alistair Scott 
the sole owner of the business with years of Corporate 
“Client Side” technical FM leadership, the team was 
quickly formed from leading Facilities Management 
(FM) business across the industry, all drawn by the 
empowerment IEM provides, made up of technical 
experts and leaders from across the FM industry, with a 
specialism of supporting clients with multi-site estates 
and a mindset of competency, clarity in support and the 
mission to make FM and building managers succeed.
 It’s about adaptability, over the first 3 years we supported 
our first client with multi sites across the UK&I (circa 
650) from a position of low compliance and control to a 
fully compliant estate supported by efficient processes 
and controls, an initial legacy that has led the confidence 
across multiple clients for IEM to support their multi
site estates and guide them on there journey to facilities 
enabling their business delivery, 85% of our clients are 
open from the outset that there compliance position 
is low and they need support, asset data is lacking and 
daily operations is reactive, IEM supports the clients on 
the journey to turn the ship around to a complaint and 
planned estate, though, reactive, planned, remedial and 
project maintenance.
 The positive culture across the IEM team and partners is 
strong, this is demonstrated with us not losing a single 
member of staff from day one, with continued growth 
to a team of 50 employee’s, and partners continually 
growing though word of mouth to work with IEM, this 
is fundamentally down to our partner support program 
(supporting SME’s), task clarity/volume and industry 
leading payment terms.
 Cox Automotive, NHS East Sussex, NHS ELFT, Eenergy, The 
Knightsbridge, Chatham House, Andrew Sykes, Strabag, 
Westminster Council, Bulgari Hotel, Stonegate Pubs and Vets 
Now, we have concurrently expanded our partner network 
deeply across the UK & Ireland, resulting in us fielding 
2500+ partners, who cover all hard services and compliance 
disciplines our revenue has increased by 100+% annually.
 The recent financial result being,
 2023 £4.5M
 2024 £15M
 The continued growth is due to our team, our industry 
leading CAFM system “Facilio” and our simple operating 
model, which is unique to the industry in that we are 
the ONLY FM company who openly shouts about us 
outsourcing the engineering delivery, which provides us 
depth of delivery, we utilise our certified supply chain 
Partners to ensure minimal travel, quick responses, and 
specialists for the work in hand.
 Accompanying this growth has been our ability to give 
back, with us being the Primary sponsor for “Scotty’s 
little Soldiers”, and the founding sponsor for the “IWFM 
Veteran’s into FM”, along with supporting more localised 
charities such as cancer survivors letter writing “From me 
to You” and “Kind Hearts”.
 Through our continued technical and leadership training 
programs, held together in clear business intent to 
support our clients on their journey, IEM have recently 
been awarded the “Best FM Company to work for 2024”.
 Professionally we are accredited by ISO 9001, 14001 & 
45001, Safe Contractor and supported by being Neutral 
Carbon Zone Platinum, as a living wage employer, we 
are also on the journey to become B-Corp accredited, 
to accompany these accreditations we are leading on 
the building compliance front as the inaugural strategic 
partnership with SFG20.
 Q2 
SERVICE DELIVERY: APPROACH
 Q: Describe how you would approach 
(including details on account management and 
helpdesk) delivery of maintenance services 
across the PortmanDentex estate including the 
organisational structure you would deploy? 
A: At IEM, we understand that delivering high-quality, 
customer-focused maintenance services across the 
Portman Dentex estate requires not only effective 
processes but also a dedicated and well-structured 
team. Our approach combines expertise from multiple 
3
PPM Team
 departments within our organisation to ensure seamless 
service delivery, clear communication, and a focus on 
continuous improvement. 
To ensure that maintenance services are delivered 
efficiently and effectively across the Portman Dentex 
estate, we would deploy a tailored team structure that 
draws from our diverse departments. This structure 
enables us to provide flexibility, accountability, and 
expertise at every stage.
 Quotations Team
 Our Quotations team is responsible for vetting and 
reviewing every quote we receive. They ensure that the 
pricing is fair, transparent, and competitive, and that all 
necessary information is included for Portman Dentex to 
make informed decisions. Our team will work closely with 
Portman Dentex to ensure that all quotations are accurate 
and aligned with your budget and expectations.
 Projects Team
 For larger projects or specific tasks requiring detailed 
oversight our Projects team, which includes project 
managers and administrators will provide dedicated 
support. They will ensure that project delivery is on track, 
within scope, and on budget. They will also work closely 
with our Helpdesk and PPM teams to ensure smooth 
coordination and execution.
 Finance and Accounts Team
 Our Accounts team will be available to support all financial 
aspects of the service, including invoice queries, payment 
tracking, and any financial reporting required by Portman 
Dentex. They will ensure transparency and accuracy in 
all financial dealings and provide timely support for any 
queries related to billing.
 Supply Chain Team
 Our Supply Chain team manages the onboarding and 
performance review of our suppliers. They ensure that we 
only work with trusted and reliable partners and conduct 
regular reviews to maintain high standards. They are 
also responsible for managing training for supply chain 
partners to ensure consistency in service delivery.
 Helpdesk Team
 We understand that communication is key. Our Helpdesk 
team will be dedicated to Portman Dentex and work 
specifically on your account. This means every time 
you contact us, you will speak with someone who fully 
understands the specifics of your account, current tasks, 
and any ongoing issues. Our clients love this personalised 
service, and it ensures efficiency in resolving queries and 
tasks. Depending on the size and needs of your estate, we 
can assign the appropriate number of helpdesk staff to 
meet the demand.
 Our PPM team will be responsible for scheduling all 
planned preventative maintenance activities, ensuring 
that these are carried out on time and in line with the 
agreed schedules. This proactive approach helps to 
minimise downtime and avoid unexpected breakdowns.
 Account Management Team
 The Account Management team will oversee the overall 
service delivery, ensuring that all departments are 
working together efficiently and that Portman Dentex’s 
needs are met. The team will track performance, monitor 
KPIs, and handle reporting to ensure accountability and 
that high standards are maintained.
 Team Deployment During Mobilisation
 When starting the partnership with Portman Dentex, we 
will deploy a mobilisation team consisting of members 
from each relevant department. This team will support 
the initial setup, ensuring that all systems, processes, 
and resources are aligned to meet your needs. The 
mobilisation team will include representatives from:
 Helpdesk: To ensure smooth onboarding of helpdesk 
staff and ensure that the account is fully understood.
 Projects: To assist with any specific projects that need 
immediate attention.
 PPM: To set up and schedule initial maintenance 
activities.
 Account Management: To manage the high-level 
coordination and ensure that all departments are 
working together efficiently.
 We are very flexible in how we work with you. For 
example, with IVC, we have a weekly call to ensure 
ongoing communication and support. For clients like 
Eenergy, we have a monthly account management call, 
tailored to their needs. We can work with Portman 
Dentex to determine the frequency and structure of these 
meetings to ensure we’re aligned with your expectations.
 Ongoing Account Management and Support
 Once mobilisation is complete, Portman Dentex will 
have a dedicated account manager who will be your 
primary point of contact. This person will oversee the 
service, coordinate between teams, and ensure that 
all feedback, issues, and requirements are addressed 
promptly. Our account management process is built 
around transparency, communication, and accountability, 
ensuring that we stay responsive and adapt to any 
changes or needs as they arise
 Additionally, our Helpdesk team will provide ongoing 
support tailored to your account. They will be familiar 
with the nuances of Portman Dentex’s requirements, 
4
 ensuring consistent, personalised service delivery
By combining the expertise of multiple departments—
 Helpdesk, Quotations, Projects, Finance, Supply Chain, and 
Account Management—we create a flexible, responsive, 
and accountable service structure that ensures high-quality 
service delivery across Portman Dentex’s estate. Our focus 
on building strong relationships and maintaining open 
communication allows us to deliver a customer-focused 
service that is always aligned with your needs.
 Q3 
SERVICE DELIVERY: SYSTEMS
 Q: Describe all the major systems you 
propose to use, including your CAFM systems 
and supporting technology. In your answer 
include data security measures to protect 
PortmanDentex data.
 A: We propose the use of Facilio as our core CAFM system 
to support Portman Dentex’s needs. This advanced system 
is fully customisable and allows us to create and adjust 
modules using an intuitive flowchart-based design. This 
f
 lexibility ensures that the system can be tailored to suit 
your preferences and operational workflows, providing 
a seamless fit for your practices. Facilio is user-friendly, 
making it easy for staff across all levels to access and utilise, 
you can access the portal through a website or via a client 
portal app, making it easy to use whilst on the move. 
It comprehensively covers FM requirements, including 
preventive maintenance schedules, all raised work orders, 
document management, all communications and more.
 The system’s real-time capabilities enhance decision
making and resource allocation, setting a new standard 
for accountability and efficiency in contract delivery. In 
addition to Facilio, our 24-hour help desk is a cornerstone 
of our service delivery. This around-the-clock support 
ensures immediate assistance for emergency tasks, 
minimising disruptions to daily activities and maintaining 
operational continuity. The help desk is seamlessly 
integrated with the system, providing a cohesive and 
responsive service experience.
 Additionally, optional modules, such as energy usage 
monitoring can be integrated if needed, offering scalability 
to meet your evolving needs.
 Facilio provides real-time data to all key stakeholders, 
ensuring transparency and enabling informed decision
making. The system aligns with IEM’s core purpose of 
simplifying the complexities of FM, making it an invaluable 
tool for managing your sites efficiently. Facilio streamlines 
operations, ensuring your practices can focus on 
delivering exceptional patient care, leaving the FM to us, 
whilst being kept well informed of progress.
 In addition to Facilio, we utilise Monday.com for internal 
project management. While this platform is primarily used 
for planning and collaboration within our team, there may be 
instances where Portman Dentex stakeholders see updates 
managed through this system. Monday.com offers robust 
functionality for tracking progress, ensuring transparency, 
and enhancing communication on collaborative projects
 At IEM, data security is a top priority. Facilio is secured 
with two-factor authentication (2FA) and single sign 
on; providing additional layers of protection against 
unauthorised access. The platform undergoes regular 
updates and testing to maintain its security standards. 
For Monday.com, we utilise an enterprise-level license 
that incorporates advanced security features, including 
encrypted data storage and role-based access controls, 
ensuring your information always remains protected.
 Beyond these measures, we implement comprehensive 
data security protocols, including GDPR-compliant data 
storage, regular penetration testing to identify and 
mitigate vulnerabilities, and ongoing employee training in 
cybersecurity best practices. These measures ensure that 
all systems we use are resilient and secure, safeguarding 
Portman Dentex’s data.
 By leveraging Facilio and Monday.com, we offer a 
sophisticated, secure, and flexible approach to Facilities 
Management. Together, these systems will streamline 
operations, ensure compliance, and provide the 
transparency and efficiency necessary.
 Q4 
SERVICE DELIVERY: 
DELIVERY MODEL
 Q: Referring to the Scope of Works in Section 
3.2 of the RFP document, confirm which of 
these categories you would self deliver, which 
sub-categories you would sub-contract and 
who you would sub-contract to. Provide further 
narrative of your preferred approach including 
any diagrams and supporting rationale if 
appropriate. Include in your response what 
measures you take to prevent your sub
contractors further sub-contracting this work.
 A: At Integrated Estate Management (IEM), we do 
not self-deliver services but instead operate through 
a network of carefully selected regional partners. This 
model ensures that we provide the best coverage and 
service quality within each geographic area, leveraging 
the expertise of locally based companies.
 For the categories and sub-categories within the Scope of 
Works, we would subcontract to these trusted partners. 
5
These partners have been rigorously vetted to meet our 
stringent standards for delivery, compliance, and customer 
satisfaction. Each partner is chosen for their proven track 
record and capability to deliver the required services to the 
highest standards within their specific region.
 Our approach offers several key advantages:
 Local Expertise: Regional partners have deep 
knowledge of their respective areas, enabling faster 
response times and better familiarity with local 
regulations and conditions.
 Quality Assurance: We maintain robust oversight 
through regular performance reviews, detailed 
Service Level Agreements (SLAs), and continuous 
communication to ensure consistent service delivery 
across all regions.
 Scalability and Coverage: This model enables us to 
provide seamless nationwide coverage, accommodating 
both routine and specialised requirements without the 
limitations of a centralised delivery model.
 To prevent subcontractors from further subcontracting 
the work, we implement the following measures:
 Contractual Provisions: Our agreements 
with subcontractors explicitly prohibit further 
subcontracting without prior written consent from IEM.
 Compliance Monitoring: We conduct regular audits 
and compliance checks to ensure that all work is 
performed directly by our contracted partners.
 Clear Communication and Reporting: Partners are 
required to provide regular updates on workforce 
allocation and service delivery to ensure alignment 
with our contractual expectations.
 Our approach ensures that clients receive reliable, high
quality service while benefiting from the flexibility and 
efficiency of our partnership model.

SERVICE DELIVERY:  
COMPLIANCE
 Q: Describe your approach to the management 
of statutory compliance, specifically how 
you would manage this for PortmanDentex, 
if successful. Within your response, provide 
examples of how you approach statutory PPMs 
and how these are identified. 
A: To ensure a smooth transition and effective compliance 
management across the estate, IEM would require 
comprehensive asset registers and the findings from the 
most recent audits to establish upcoming compliance 
dates. This would include lifecycle information where 
available. Should these records be incomplete or 
unavailable, we would collaborate with Portman Dentex 
to propose an asset verification survey across the estate 
to gather the necessary data.
 Using this information, IEM would review the asset details 
and develop a tailored PPM schedule based on SFG20 
standards and/or manufacturer recommendations. Our 
CAFM system, Facilio, offers an advanced scheduling 
mechanism that generates an SLA window ahead of each 
compliance date. This window is incorporated into task 
work orders, allowing the service partner to attend within 
a specified timeframe while also accounting for site access 
arrangements.
 Facilio’s dashboards highlight tasks at risk of non
compliance—whether due to a delay in ETA confirmation 
or proximity to the SLA end date. These risks are actively 
managed by our compliance team, ensuring timely 
delivery. Completed tasks are not marked as such until 
all associated documentation has been reviewed and 
approved.
 We continuously monitor supply chain performance, 
with Facilio’s algorithm scoring service partners on their 
delivery standards. These scores directly impact future 
work allocations and form a key part of supply chain 
performance reviews.
 To further enhance risk management, we recommend 
establishing a Risk Management Steering Group. This 
group would focus on tracking high-risk remedial works, 
compliance issues, and the development of a forward 
maintenance register. Regular meetings would address 
estate strategies, budgets, and current compliance 
challenges, including any backlog of works.
 One of our current clients lacked a comprehensive 
compliance or asset data set. We worked closely with 
them to compile this information while implementing 
a bespoke maintenance regime across their estate. 
Our involvement included organising Health and Safety 
Steering Group meetings, developing high-risk registers, 
and agreeing on weekly actions to review risks and 
budgets.
 Additionally, we prioritised high-risk buildings and 
unknown assets by tailoring a PPM schedule to address 
these areas as a priority. This proactive approach has 
helped them achieve compliance while building a robust 
strategy for future maintenance.
 6
Q6 
Q7 
SERVICE DELIVERY:  
QUALITY ASSURANCE
 Q: Describe your approach to quality assurance 
across all services. 
A: At IEM, quality assurance is more than just a process—
 it is embedded in everything we do, from the way we 
collaborate with clients to how we train our teams and 
select our partners. Our approach is rooted in adaptability, 
personalisation, and a shared commitment to achieving 
excellence.
 We provide clients with extensive analytics through 
bespoke dashboards, offering real-time insights and 
detailed reports. This allows us to monitor trends, identify 
potential risks, and implement proactive solutions. 
By leveraging these tools, we ensure that issues are 
addressed before they arise, keeping operations seamless 
and efficient. For existing clients, we have developed 
tailored risk management documents, identifying all FM
related risks to support their ability to manage challenges 
effectively, further reinforcing our commitment to quality.
 Our dedication to excellence extends to our team, 
who have recently completed CPD-certified in-person 
customer service training sessions. This investment 
ensures they are equipped to deliver an outstanding, 
client-focused experience. Our efforts have not gone 
unnoticed—we were recently awarded ‘Best Company 
to Work For’ at the FM and Property Anticipate Awards, 
reflecting the strength of our team and the quality we 
bring to our clients.
 At IEM, collaboration is key. We do not see ourselves as 
just a service provider but as a partner. Our personalised 
approach allows us to work closely with clients to align on 
goals, overcome challenges, and achieve success together. 
This is not your typical FM relationship—it is a partnership 
driven by shared goals and a desire for greatness.
 To uphold our high standards, we carefully vet all 
partners. Each must have an SSIP accreditation, and we 
strongly recommend SafeContractor status, ensuring that 
everyone working on your sites is qualified and aligned 
with our rigorous quality requirements.
 From analytics and risk management to collaboration and 
partner integrity, we ensure quality at every level. Our 
size and structure enable us to provide a highly tailored 
service that larger providers simply cannot match. This 
dedication to adaptability, innovation, and collaboration is 
what sets us apart and ensures exceptional outcomes for 
our clients.
 SERVICE DELIVERY: 
CUSTOMER SATISFACTION
 Q: How do you ensure customer satisfaction 
and what is the process for signing off works 
after they have been completed? Do you 
ask the question ‘Are you satisfied with the 
works? What role do you envisage the Practice 
Managers playing in this regard?
 A: We prioritise customer satisfaction through a 
structured and transparent process. Upon the completion 
of works the Practice Manager will be requested to sign 
off the engineers works via the Facilio engineer app 
confirming they are happy with the works carried out, 
these details are then added to the portal and visible for 
all that have access to that specific site (such as Practice 
Manager, Area Managers, FM Managers, IEM and our 
Supply Chain Partner).
 Our usual model, which we find works brilliantly, is to have 
dedicated Helpdesk members for each client, this means 
that your Sites and Teams are always talking to the same 
people, giving them to chance to build great relationships 
and really work together. This also gives our Helpdesk 
team the opportunity to really learn the ins and outs of 
your Practices and give the best service possible. With our 
larger clients such as IVC where there are many sites, to 
make the experience even more personalised, we split the 
team per region, so each specific region has a dedicated 
contact they speak to. Our Helpdesk team are then able 
to work with the Sites/regional FM managers etc. and 
learn how they prefer to work, some like to have a regular 
teams call to catch ups, others prefer contact via the note 
of the portal only – By working this way gives us flexibility 
to provide a much more personal service to you.
 Following the task completion we then have a customer 
feedback module of the system where we can collate 
feedback from Practice Managers for their completed 
works, this is a straightforward process where we ask them 
to choose between a happy, neutral or unhappy face, 
with the chance to give text feedback and answer a few 
questions on the service they received, the system then 
reports on this data to ensure all relevant stakeholders have 
visibility of our performance. Our Account Management 
Team, along with our Business Excellence department also 
review this data on a regular basis to ensure continuously 
improvement within our company.
 Innovation and Continuous Improvement for us is at the 
heart of our business ethos, driving us to consistently 
enhance our services, exceed client expectations, and 
adapt to ever-changing industry demands by listening 
to feedback, embracing new ideas, and implementing 
effective solutions that deliver measurable value.
 7
Q8 
Q9 
SERVICE DELIVERY: 
REMEDIALS
 Q: Describe your approach to dealing with 
Remedial Works for PortmanDentex. Consider 
in your response how you could bundle works 
to maximise risk mitigation, efficiency and 
cost effectiveness and process for escalations 
to expedite work if required. How will you 
demonstrate cost effectiveness versus the market? 
A: IEM adopts a comprehensive and cost-effective 
approach to remedial works. We begin with a thorough 
assessment to identify the required actions and 
opportunities to bundle remedials wherever possible. By 
coordinating works efficiently, we minimise disruption, 
reduce engineer attendance fees, and lower overall 
remedial costs, ensuring the best value for our clients.
 This strategy has been successfully implemented with 
partners such as NHS West Suffolk Trust and Arnold 
Clark. For example, within our PPM department, we 
have a dedicated remedial team that ensures all planned 
preventative maintenance (PPM) tasks are completed 
end-to-end, with full certification of compliance.
 By adopting this approach, PortmanDentex will benefit 
from a streamlined and compliant estate management 
process. Our CAFM system, Facilio, provides real-time 
visibility, allowing the client to monitor compliance and 
progress on-site at any time.
 SPECIALIST DENTAL SERVICES
 Q: Specialist Dental Services (as defined in 
3.2.3 of the RFP document) are out of scope 
of this RFP. However, PortmanDentex would 
like to understand the potential operational 
and commercial viability of the Service 
Provider providing Helpdesk services as well as 
overseeing the management, reactive call outs, 
PPMs and other services provided by specialist 
dental suppliers (e.g. Henry Schein, DD Group, 
Hague Dental etc.) 
Please describe how this could work, what your suggested 
commercial model would be and, if you have experience in 
the dental sector, is this something that you already do?
 A: At IEM, we are flexible in managing your existing 
contractors, and we would be happy to onboard your 
current specialist dental suppliers to work alongside us 
and our current Supply Chain. Our recommendation is 
to centralise all information in Facilio, which allows for 
seamless task tracking, reporting, and transparency. 
This approach ensures that all contractor activity is 
consolidated, making it easier to monitor performance, 
identify trends, and maintain service consistency.
 We would recommend adding an agreed management 
mark-up percentage to each task undertaken by your 
specialist contractors. This is a simple and transparent way 
to manage costs while ensuring effective oversight and 
coordination.
 Once onboarded, all contractors would be subject to 
our performance monitoring protocols. Using Facilio, 
we would track task completion times, compliance with 
SLAs, and overall service quality. Regular reporting would 
be provided to you, ensuring full visibility of contractor 
performance and identifying areas for improvement 
where necessary.
 Although we do not currently manage specialist dental 
equipment, we have significant experience working with 
clients in related sectors, such as veterinary practices. 
In these settings, we frequently support with specialist 
equipment, including compliance with x-ray and Radiation 
Protection Adviser (RPA) requirements. Our understanding 
of high-compliance environments ensures we can quickly 
adapt to the needs of the dental sector and bring valuable 
insights to managing similar specialist equipment.
 We are confident in our ability to seamlessly integrate 
your existing contractors into our processes, providing 
a centralised, efficient, and transparent solution that 
enhances oversight and supports your operational goals.
 8
Q10
 3. Sealing and Welding for Infection Control:
 CLINICAL / MEDICAL  
ENVIRONMENT EXPERIENCE
 Q: Describe your capability and experience in 
working in regulated clinical environments such 
as dental surgeries and provide examples of 
work you have completed in such environments. 
Give examples of the regulators and regulations 
you may need to consider undertaking these 
works. At PortmanDentex there will be clinical 
compliance remedial activity such as lead lining, 
sealing/welding of floors, sealing of worktops 
etc. that we have historically used specialist 
dental contractors to carry out. Do you have 
experience in carrying out these works in a 
regulated medical / clinical environment? 
What would your approach be to these clinical 
compliance remedial works?
 A: At IEM, we have experience working in regulated 
clinical environments, including veterinary practices, 
which share many operational and compliance similarities 
with dental surgeries. These include stringent regulations 
around radiation protection, infection control, and clinical 
compliance. Our work in these settings has equipped us 
with the skills, knowledge, and partnerships to confidently 
handle dental surgery environments with precision and 
compliance.
 Specific Experience and Expertise
 1. Radiation Compliance and X-Ray Equipment:
 We collaborate with a highly skilled team that 
specialises in x-ray electrical works nationwide.
 They have deep expertise in working with Radiation 
Protection Advisers (RPAs) such as Stephen and Green 
Associates, ensuring compliance with IRR17 (Ionising 
Radiations Regulations 2017).
 An example includes the installation of systems 
where x-ray warning lights are interlocked to prevent 
the machine’s operation in case of light failure, a 
requirement often overlooked by other contractors.
 2. Lead Lining and Radiation Protection:
 Our teams are experienced in installing lead-lined 
solutions, including lead-lined blinds, doors, and wall 
boarding.
 In a recent project, we worked with a veterinary 
client to ensure compliance with radiation shielding 
standards, delivering a solution that included lead
lined partition walls and doorways, certified to meet 
regulatory requirements.
 Infection control is a critical aspect of clinical 
environments, and we have a proven track record in 
sealing and welding works.
 For example, we’ve successfully sealed floors 
and worktops in high-risk clinical areas to ensure 
compliance with infection prevention regulations, 
using materials approved for medical settings.
 We ensure all works align with the relevant 
regulations and guidelines, including:
 Health and Safety Executive (HSE) guidelines for 
clinical compliance.
 Control of Substances Hazardous to Health (COSHH) 
for managing materials used in clinical spaces.
 HTM (Health Technical Memoranda) for flooring, 
worktops, and infection control.
 IRR17 and associated guidance for radiation 
protection.
 Approach to Clinical Compliance  
Remedial Works
 1. Detailed Assessment and Planning:
 Conduct a thorough site survey and consult with 
relevant stakeholders, including RPAs, infection 
control specialists, and facility managers.
 Provide a detailed risk assessment and method 
statement (RAMS) tailored to the specific 
requirements of the clinical environment.
 2. Use of Specialist Contractors and Materials:
 Engage trusted specialists with experience in 
regulated environments, ensuring all works are 
completed to the highest standard.
 Use materials certified for medical and clinical use, 
such as antimicrobial surfaces for sealing worktops 
and flooring.
 3. Compliance-Driven Execution:
 Carry out works in compliance with HTM and 
infection control standards, ensuring minimal 
disruption to clinical operations.
 Maintain robust communication with the client 
throughout, providing progress updates and 
compliance documentation as needed.
 4. Post-Completion Validation:
 Conduct a full inspection and testing to confirm 
compliance with relevant regulations.
 Provide clients with a compliance pack, including 
certifications, photographs, and reports for their 
records.
 9
Examples of Relevant Work
 sites. With this system in place, any queries or issues are 
Veterinary Practice Refurbishments: Delivered radiation 
protection upgrades, including lead lining and x-ray 
warning systems, ensuring compliance with IRR17.
 Clinical Fit-Outs: Completed floor and worktop sealing 
projects in regulated clinical spaces, achieving infection 
control compliance.
 At IEM, we bring a proven track record of success in 
regulated environments and a proactive, compliance-first 
approach. Our team is well-equipped to meet Portman 
Dentex’s requirements for clinical compliance remedial 
works, ensuring your facilities remain operational, 
compliant, and ready to serve patients effectively.
 Q11
 CUSTOMER SERVICE
 Q: With relevant examples, provide a description 
of how would you organise a high quality, 
customer focused service for PortmanDentex. 
Please describe your approach to: – Customer Helpdesk – Compliments and Complaints – Customer Service training for your staff– Monitoring and reporting on levels of customer 
satisfaction – Communication– How you would ensure the customer (particularly 
in practice) is kept informed  
and engaged– Ensuring appropriate conduct of your 
representatives whilst on site
 A: At IEM, we are committed to delivering a high-quality, 
customer-focused service that not only meets but exceeds 
Portman Dentex’s needs. We understand that exceptional 
service is the foundation of a successful partnership, and 
we are dedicated to providing a seamless and responsive 
service that supports the operational efficiency and 
satisfaction of your practices.
 Efficient and Responsive Customer Helpdesk
 We recognise the importance of having an efficient and 
responsive customer helpdesk. Our helpdesk operates 
24/7/365, ensuring that Portman Dentex’s needs are met 
promptly, no matter the time of day. The Facilio system is 
at the heart of our helpdesk operations, enabling real
t
 ime monitoring and swift issue resolution; due to the 
automations in the system such as chasing overdue tasks 
with our Partners and assigning works (after they have 
been fully vetted), means it frees up our team’s time to 
focus on what really matters, communicating with the 
captured immediately, allowing us to address them without 
delay. This ensures the smooth operation of your practices 
and enables us to keep things running efficiently, reducing 
downtime and preventing unnecessary disruptions.
 Proactive Management of Compliments and Complaints 
Our approach to managing compliments and complaints 
is both proactive and systematic. We have a dedicated 
team responsible for handling feedback, ensuring that 
all compliments are acknowledged and shared with the 
relevant teams to reinforce positive behaviour. We take 
complaints seriously—each one is logged, thoroughly 
investigated, and resolved promptly. Root cause analysis 
is conducted to identify the underlying causes and ensure 
that similar issues do not recur. We track all complaints 
and escalations through our Account Management team, 
who provide regular updates to the complainant and 
review any escalations during our weekly calls with IVC, 
although these instances are minimal.
 Training and Development of Our Team
 At IEM, we believe in the value of our people, which 
is why we invest in their continuous professional 
development. All of our staff undergo comprehensive 
customer service training during their initial training and 
probation period before they are fully integrated into their 
respective accounts. This training covers essential skills 
such as communication, empathy, problem-solving, and 
the ins and outs of Facilities Management.
 We are proud of our commitment to our team’s 
progression, which has been recognised with our recent 
award for Best Company to Work For at the FM and 
Property Anticipate Awards. Additionally, our entire IEM 
team have recently completed CPD-certified customer 
service training, including modules on delivering 
excellence and dealing with challenging situations.
 Our team’s development continues with site visits to 
their relevant accounts and support with their Personal 
Development Plans. This ensures that they remain adept 
at providing exceptional service and are continuously 
improving to meet the needs of Portman Dentex.
 Monitoring and Reporting Customer Satisfaction 
We actively monitor and report on levels of customer 
satisfaction through multiple methods, such as regular 
surveys, feedback forms, and direct interviews. The 
feedback gathered is carefully analysed to identify trends 
and areas for improvement. This data is used to inform 
future actions, ensuring that service delivery is consistently 
enhanced. We will provide detailed reports to Portman 
Dentex, highlighting our performance and any corrective 
actions we have taken to improve service quality.
 In addition to our regular surveys, our Facilio system 
includes a feedback module, where sites can provide 
feedback on each completed task. This allows Portman 
10
Dentex to review the service provided and track performance 
Q12
 on an ongoing basis, ensuring continuous improvement.
 Communication and Customer Engagement
 Effective communication is central to our service delivery. 
We ensure that communication remains clear and 
consistent through multiple channels, including emails, 
phone calls, and in-person meetings. Our helpdesk team 
is organised by specific clients and even regions for larger 
clients like Portman Dentex, ensuring a personalised 
service for every site.
 To keep Portman Dentex engaged, we implement a 
structured communication plan that includes scheduled 
meetings, progress reports, and feedback sessions. Your 
dedicated Helpdesk member(s) will be the first point 
of contact for day to day queries etc, you then have 
a dedicated account manager who will act as a single 
point of contact working with your FM team, ensuring 
streamlined and effective communication. Additionally, 
our CAFM system provides real-time updates on service 
status, so you are always informed and up-to-date on any 
ongoing activities or potential issues.
 Ensuring Appropriate Conduct On-Site
 All of our representatives are trained to uphold the 
highest standards of professionalism and conduct while 
on site. This includes adherence to Portman Dentex’s 
policies and procedures, maintaining a respectful and 
courteous demeanour, and ensuring minimal disruption 
to your operations. We conduct regular audits and have 
feedback mechanisms in place to monitor and reinforce 
appropriate behaviour. All of our Supply Chain Partners 
have to go through an in-depth onboarding process, to 
ensure their values align with ours and that they are the 
right teams for the tasks in hand, that we can trust to 
support us.
 Outcomes and Benefits
 By organising a high-quality, customer-focused service, 
Portman Dentex will benefit from enhanced operational 
efficiency, increased customer satisfaction, and a 
stronger reputation for delivering exceptional service. 
Our approach ensures that your needs are met promptly, 
feedback is handled effectively, and communication 
remains clear and consistent. Ultimately, this will support 
the success and growth of your practices, creating an 
environment where patients and staff can thrive.
 REFERENCES
 Q: Please provide two customer references that 
are relevant to services requested in this RFP 
and that are currently being provided by your 
company. 
Please provide the name, job title, email address and phone 
numbers of the referees as well as a full description of the 
services that you are providing to these customers. Please 
ensure that references provide an comparable level of service 
to what PotmanDentex are looking for. 
Anthony Hind
 07816 202692
 antony.hind@ivcevidensia.com
 David Stevens
 07490730355
 david.stevens18@nhs.net
 11
Q13
 REPORTING / MANAGEMENT 
INFORMATION
 Q: What Management Information can you 
provide to PortmanDentex? 
Please provide examples of reports and management 
information you provide to your existing clients. Include in 
your answer considerations regarding monitoring of trends 
such as repeated call outs to the same asset and preventative 
actions to stop this to reoccurring. 
What financial and helpdesk statistics would you recommend 
we monitor and report on?
 A: At IEM, we take great pride in offering comprehensive 
management information to support Portman Dentex’s 
operational goals, improve efficiency, and ensure 
informed decision-making. We understand that timely, 
actionable insights are key to driving performance, and we 
are committed to providing you with the data you need 
to optimise your operations, reduce costs, and improve 
service delivery. Our system allows us to manage the 
reporting with complete flexibility, where we can add/
 remove particular reporting based on the user level and 
what you would like to see.
 Key Management Information Reports
 1. Operational Task Overview
 We will provide a detailed breakdown of outstanding tasks 
by site, area, building, or region, ensuring visibility into the 
entire estate. This includes tracking tasks that are awaiting 
IEM vetting, require additional information, or are split 
by the stage of completion such as awaiting scheduling, 
scheduled awaiting attendance, or complete. We will also 
monitor tasks by discipline, ensuring the right teams are 
allocated to the appropriate work.
 Total in SLA / Out of SLA: Visual reporting such as pie 
charts will provide clarity on the percentage of tasks 
meeting Service Level Agreements (SLAs). This will allow 
Portman Dentex to track the efficiency of reactive work, 
quotes, and PPM.
 2. Quotes Tracking
 A comprehensive overview of all outstanding quotes, 
including those awaiting submission, review, or client 
approval, will be provided. We can break down these 
quotes per discipline, region etc, ensuring transparency 
and enabling you to stay on top of pending quotes. 
Additionally, tracking the average task acceptance time 
and attendance and completion times will give you 
real-time visibility into task performance and allow for 
improvements where necessary.
 First-Time Fix Rate: We can also track the first-time fix 
percentage to assess how often we are able to resolve 
issues on the first visit, reducing repeat visits and 
improving operational efficiency.
 3. Preventative Maintenance (PPM) Overview
 To help prevent recurring issues, we will provide a detailed 
breakdown of outstanding PPMs, including the status of 
tasks such as awaiting scheduling, scheduled awaiting 
attendance, and tasks requiring another visit. By tracking 
SLA compliance and categorising tasks by discipline, 
we can ensure timely and effective maintenance. This 
proactive approach will help reduce repeated call-outs to 
the same assets, preventing failures and ensuring long
term asset reliability.
 Monitoring Trends and Preventing Recurring Issues 
One of the most significant aspects of our management 
information reporting is the ability to track trends 
in repeated call-outs to the same assets. By closely 
monitoring these trends, we can identify potential 
underlying issues, whether they are due to poor 
asset condition, incorrect installation, or insufficient 
maintenance. Our proactive approach enables us to 
implement preventative actions to address these issues 
before they escalate, such as adjusting maintenance 
schedules, recommending upgrades, or providing training 
to ensure staff handle equipment correctly.
 We also recommend monitoring warranty percentages 
and recall rates for assets, which help ensure that assets 
under warranty are operating as expected and that any 
product recalls are managed efficiently.
 Financial and Helpdesk Statistics
 In addition to operational and PPM reporting, we can also 
report on financial statistics to improve service delivery 
and cost management:
 Total Spend per Month: Split into quotes, reactive 
maintenance, and PPM, providing insight into cost 
distribution and opportunities for savings.
 Accrued Costs: Split into completed and not yet 
completed tasks to provide visibility into outstanding 
f
 inancial obligations.
 Helpdesk Metrics: Track response times, resolution times, 
and task acceptance rates to measure the efficiency of 
the helpdesk in addressing queries and maintenance 
requests.
 Live Data for Real-Time Decision-Making
 All the above reports and insights can be made available 
in real-time via our Facilio dashboard. This means that 
Portman Dentex can access live data without having to 
wait for periodic reports, enabling you to make timely, 
informed decisions. The dashboard will be tailored to 
your needs and will be updated continuously, providing 
transparency and helping to optimise resource allocation 
12
and operational performance.
 Examples of these are as follows:
 By partnering with IEM, Portman Dentex will benefit from 
a robust suite of management reports that give complete 
visibility into your operations. Our real-time data tracking, 
combined with proactive maintenance strategies, will 
not only help reduce asset failure rates but also enable 
you to make strategic decisions with confidence. These 
non-financial benefits will ultimately improve operational 
efficiency, reduce unnecessary costs, and enhance the 
overall service quality.
 Please refer to the example reports in the appendix, 
sections 1.1 through 1.7.
 Q14
 COMMERCIAL MODEL
 Q: Describe your preferred approach for pricing 
maintenance services. If there is an alternative 
model that you believe PortmanDentex should 
consider, please put forward an alternative 
pricing proposal in addition to the format 
requested in Appendix 2 - Pricing Template
 We recommend adopting the pricing model outlined 
in the attached pricing template, as the most suitable 
commercial model for maintenance services.
 This model provides a clear, transparent, and structured 
approach to pricing, ensuring consistency and ease of 
understanding for both parties.
 While we believe the attached model is the most 
appropriate option, we are open to discussing alternative 
approaches should PortmanDentex have additional 
considerations or priorities that necessitate a bespoke 
solution.
 Q15 
FINANCIAL BENEFITS
 Q: Describe the financial benefits which you 
believe you can deliver to PortmanDentex and 
include a rationale for why you think you can 
deliver these benefits. 
Provide a glidepath of savings opportunities over a 5 
year period and state your assumptions. What savings 
opportunities and/or efficiencies do you envisage for 
PortmanDentex? How will you help us realise them?
 A: IEM can deliver significant financial benefits to 
PortmanDentex by identifying, implementing, and 
sustaining savings opportunities across procurement, 
operations, and workforce efficiencies. 
Streamlining the supply chain and focusing on preferred 
suppliers will lead to beneficial rates and reduced 
administrative overheads
 Automation through the introduction of IEM’s CAFM 
system will lower administrative costs and increase the 
availability and accuracy of commercial reporting. This 
will lead to knowledge based strategic decision making 
directly impacting the potential for operational savings
 The following categories can be utilised to enhance the 
financial benefits to PortmanDentex:
 Data-Driven Approach:
 Regularly analyse procurement and operational data to 
identify trends and opportunities.
 Technology Implementation:
 Deploy scalable digital solutions to drive automation and 
efficiencies.
 Continuous Improvement:
 Establish a culture of continuous improvement across all 
clinics with KPIs to track progress.
 Change Management:
 Engage stakeholders and provide training to ensure 
smooth adoption of new practices.

e patients and staff can thrive.
 REFERENCES
 Q: Please provide two customer references that 
are relevant to services requested in this RFP 
and that are currently being provided by your 
company. 
Please provide the name, job title, email address and phone 
numbers of the referees as well as a full description of the 
services that you are providing to these customers. Please 
ensure that references provide an comparable level of service 
to what PotmanDentex are looking for. 
Anthony Hind
 07816 202692
 antony.hind@ivcevidensia.com
 David Stevens
 07490730355
 david.stevens18@nhs.net
 11
Q13
 REPORTING / MANAGEMENT 
INFORMATION
 Q: What Management Information can you 
provide to PortmanDentex? 
Please provide examples of reports and management 
information you provide to your existing clients. Include in 
your answer considerations regarding monitoring of trends 
such as repeated call outs to the same asset and preventative 
actions to stop this to reoccurring. 
What financial and helpdesk statistics would you recommend 
we monitor and report on?
 A: At IEM, we take great pride in offering comprehensive 
management information to support Portman Dentex’s 
operational goals, improve efficiency, and ensure 
informed decision-making. We understand that timely, 
actionable insights are key to driving performance, and we 
are committed to providing you with the data you need 
to optimise your operations, reduce costs, and improve 
service delivery. Our system allows us to manage the 
reporting with complete flexibility, where we can add/
 remove particular reporting based on the user level and 
what you would like to see.
 Key Management Information Reports
 1. Operational Task Overview
 We will provide a detailed breakdown of outstanding tasks 
by site, area, building, or region, ensuring visibility into the 
entire estate. This includes tracking tasks that are awaiting 
IEM vetting, require additional information, or are split 
by the stage of completion such as awaiting scheduling, 
scheduled awaiting attendance, or complete. We will also 
monitor tasks by discipline, ensuring the right teams are 
allocated to the appropriate work.
 Total in SLA / Out of SLA: Visual reporting such as pie 
charts will provide clarity on the percentage of tasks 
meeting Service Level Agreements (SLAs). This will allow 
Portman Dentex to track the efficiency of reactive work, 
quotes, and PPM.
 2. Quotes Tracking
 A comprehensive overview of all outstanding quotes, 
including those awaiting submission, review, or client 
approval, will be provided. We can break down these 
quotes per discipline, region etc, ensuring transparency 
and enabling you to stay on top of pending quotes. 
Additionally, tracking the average task acceptance time 
and attendance and completion times will give you 
real-time visibility into task performance and allow for 
improvements where necessary.
 First-Time Fix Rate: We can also track the first-time fix 
percentage to assess how often we are able to resolve 
issues on the first visit, reducing repeat visits and 
improving operational efficiency.
 3. Preventative Maintenance (PPM) Overview
 To help prevent recurring issues, we will provide a detailed 
breakdown of outstanding PPMs, including the status of 
tasks such as awaiting scheduling, scheduled awaiting 
attendance, and tasks requiring another visit. By tracking 
SLA compliance and categorising tasks by discipline, 
we can ensure timely and effective maintenance. This 
proactive approach will help reduce repeated call-outs to 
the same assets, preventing failures and ensuring long
term asset reliability.
 Monitoring Trends and Preventing Recurring Issues 
One of the most significant aspects of our management 
information reporting is the ability to track trends 
in repeated call-outs to the same assets. By closely 
monitoring these trends, we can identify potential 
underlying issues, whether they are due to poor 
asset condition, incorrect installation, or insufficient 
maintenance. Our proactive approach enables us to 
implement preventative actions to address these issues 
before they escalate, such as adjusting maintenance 
schedules, recommending upgrades, or providing training 
to ensure staff handle equipment correctly.
 We also recommend monitoring warranty percentages 
and recall rates for assets, which help ensure that assets 
under warranty are operating as expected and that any 
product recalls are managed efficiently.
 Financial and Helpdesk Statistics
 In addition to operational and PPM reporting, we can also 
report on financial statistics to improve service delivery 
and cost management:
 Total Spend per Month: Split into quotes, reactive 
maintenance, and PPM, providing insight into cost 
distribution and opportunities for savings.
 Accrued Costs: Split into completed and not yet 
completed tasks to provide visibility into outstanding 
f
 inancial obligations.
 Helpdesk Metrics: Track response times, resolution times, 
and task acceptance rates to measure the efficiency of 
the helpdesk in addressing queries and maintenance 
requests.
 Live Data for Real-Time Decision-Making
 All the above reports and insights can be made available 
in real-time via our Facilio dashboard. This means that 
Portman Dentex can access live data without having to 
wait for periodic reports, enabling you to make timely, 
informed decisions. The dashboard will be tailored to 
your needs and will be updated continuously, providing 
transparency and helping to optimise resource allocation 
12
and operational performance.
 Examples of these are as follows:
 By partnering with IEM, Portman Dentex will benefit from 
a robust suite of management reports that give complete 
visibility into your operations. Our real-time data tracking, 
combined with proactive maintenance strategies, will 
not only help reduce asset failure rates but also enable 
you to make strategic decisions with confidence. These 
non-financial benefits will ultimately improve operational 
efficiency, reduce unnecessary costs, and enhance the 
overall service quality.
 Please refer to the example reports in the appendix, 
sections 1.1 through 1.7.
 Q14
 COMMERCIAL MODEL
 Q: Describe your preferred approach for pricing 
maintenance services. If there is an alternative 
model that you believe PortmanDentex should 
consider, please put forward an alternative 
pricing proposal in addition to the format 
requested in Appendix 2 - Pricing Template
 We recommend adopting the pricing model outlined 
in the attached pricing template, as the most suitable 
commercial model for maintenance services.
 This model provides a clear, transparent, and structured 
approach to pricing, ensuring consistency and ease of 
understanding for both parties.
 While we believe the attached model is the most 
appropriate option, we are open to discussing alternative 
approaches should PortmanDentex have additional 
considerations or priorities that necessitate a bespoke 
solution.
 Q15 
FINANCIAL BENEFITS
 Q: Describe the financial benefits which you 
believe you can deliver to PortmanDentex and 
include a rationale for why you think you can 
deliver these benefits. 
Provide a glidepath of savings opportunities over a 5 
year period and state your assumptions. What savings 
opportunities and/or efficiencies do you envisage for 
PortmanDentex? How will you help us realise them?
 A: IEM can deliver significant financial benefits to 
PortmanDentex by identifying, implementing, and 
sustaining savings opportunities across procurement, 
operations, and workforce efficiencies. 
Streamlining the supply chain and focusing on preferred 
suppliers will lead to beneficial rates and reduced 
administrative overheads
 Automation through the introduction of IEM’s CAFM 
system will lower administrative costs and increase the 
availability and accuracy of commercial reporting. This 
will lead to knowledge based strategic decision making 
directly impacting the potential for operational savings
 The following categories can be utilised to enhance the 
f
 inancial benefits to PortmanDentex:
 Data-Driven Approach:
 Regularly analyse procurement and operational data to 
identify trends and opportunities.
 Technology Implementation:
 Deploy scalable digital solutions to drive automation and 
efficiencies.
 Continuous Improvement:
 Establish a culture of continuous improvement across all 
clinics with KPIs to track progress.
 Change Management:
 Engage stakeholders and provide training to ensure 
smooth adoption of new practices
 Q16 
NON-FINANCIAL BENEFITS
 Q: Describe the non-financial benefits which you 
believe you can deliver to PortmanDentex, for 
example:– Reduced asset failure– Better management information informing 
strategic decision making – Improved customer communication 
For each benefit include how it will be delivered, how it will be 
funded and how it will enhance the PortmanDentex business. 
A: We are committed to delivering non-financial benefits 
that go beyond simply meeting service requirements. We 
understand that our role is not just about maintaining 
infrastructure but also about enhancing Portman Dentex’s 
operations, improving employee and patient satisfaction, 
and supporting long-term strategic goals.
 Reduced Asset Failure
 One of the key benefits we can bring is reduced 
asset failure. We will implement a proactive Planned 
Preventative Maintenance (PPM) schedule, tailored 
to Portman Dentex’s estate and aligned with industry 
standards like SFG20. By proactively managing assets, 
13
using real-time monitoring tools, and addressing issues 
before they become problems, we will reduce the risk 
of unexpected breakdowns. This will not only keep your 
operations running smoothly but also create a more 
reliable environment for your patients and staff.
 Better Management Information Informing 
Strategic Decision Making
 In terms of decision-making, our approach focuses on 
delivering better management information that informs 
strategic choices. Using our Facilio system, we will provide 
detailed, real-time management reports that highlight key 
performance indicators and compliance status. With asset 
condition surveys and comprehensive data-driven insights, 
your team will be able to make informed decisions about 
future investments and long-term planning. This will help 
ensure resources are used effectively and that you can 
plan for the future with confidence.
 Improved Customer Communication
 We understand that clear and transparent customer 
communication is crucial. To support this, we have 
our 24/7 dedicated helpdesk to hand, providing quick 
responses to maintenance requests and customer 
inquiries. Additionally, we will implement a feedback 
loop, allowing your team and patients to share their 
thoughts on our services, which will help us continuously 
improve. By staying connected and ensuring open lines of 
communication, we will build stronger relationships with 
your stakeholders and enhance overall satisfaction.
 We pride ourselves on being flexible in how we support 
Portman Dentex. While we strongly recommend using our 
CAFM system for its seamless integration and efficiency, 
we understand that different needs arise. Therefore, we 
are also happy to provide support via phone or email, 
ensuring that your team can reach us in the way that is 
most convenient for them. Of course, using the system 
ensures the best efficiency and tracking, but we’re here to 
adapt to your preferences.
 Compliance and Risk Management
 Ensuring that Portman Dentex operates in full compliance 
with regulatory requirements is a top priority. We will 
conduct regular audits and maintain a Golden Thread of 
Information for all legal and statutory documentation. By 
staying on top of these requirements, we can reduce legal 
risks, provide peace of mind, and support Portman Dentex 
in its role as a responsible, compliant healthcare provider. 
This proactive approach will help mitigate potential issues 
and allow you to focus on providing excellent care.
 Training and Development
 Training and upskilling are vital for long-term success, 
which is why we will provide tailored training programs for 
key staff at Portman Dentex. Whether it’s using our CAFM 
system or understanding compliance protocols, we’ll 
ensure your team feels confident and knowledgeable. 
Additionally, we’ll provide refresher courses and regular 
knowledge-sharing sessions to keep skills sharp. This 
investment in your people will ensure everyone is fully 
equipped to handle day-to-day needs and unexpected 
challenges.
 By partnering with IEM, you’ll gain more than just 
reliable facilities management. You’ll benefit from a 
comprehensive, proactive approach that adds value in 
ways that truly matter to your business and the people it 
serves. We’re here to help Portman Dentex thrive—both 
operationally and in creating a positive environment for 
your patients, staff, and stakeholders.
 Q17 
IMPROVEMENTS
 Q: Having reviewed the information within 
the RFP, what opportunities do you see for 
PortmanDetnex to improve the delivery of 
maintenance throughout it’s estate? Within 
your answer, draw on your experience from your 
clients who have a similar portfolio of properties 
to PortmanDentex, what our competitors are 
doing and what is best in class in the industry. 
A: Building on our extensive experience with clients 
managing similar property portfolios, we have identified 
key opportunities to optimise maintenance operations 
across the PortmanDentex estate. Our bespoke solutions 
are designed to deliver measurable benefits, ensuring 
operational excellence and long-term success.
 Our Solutions
 1. Preventive Maintenance Programmes
 Developing and implementing comprehensive preventive 
maintenance schedules, aligned with detailed asset 
registers, will enable PortmanDentex to proactively 
address potential issues. This approach minimises 
disruptions, avoids costly repairs, and ensures that 
critical equipment and facilities are maintained in optimal 
condition.
 2.Integration of Advanced Technologies
 Leveraging advanced technologies, such as the Facilio 
CAFM system, will transform maintenance operations by:
 Streamlining work order management.
 Centralising property-related information through 
integrated systems.
 Utilising built-in analytics to track trends, forecast 
asset replacement needs, and align with energy 
management strategies.
 14
Q17.1 
This integration allows for real-time oversight of 
maintenance activities, enabling data-driven decisions 
that enhance operational efficiency.
 3. Skilled Workforce and Continuous Training
 Ensuring that maintenance teams are well-trained, 
certified, and equipped with the latest industry knowledge 
is essential. IEM works closely with SFG-20 on ongoing 
training and development programmes will help maintain 
high standards of service delivery while keeping staff up
to-date with emerging technologies and best practices.
 4. Enhanced Asset Management
 Implementing robust asset management systems will 
facilitate effective monitoring of equipment conditions, 
proactive planning for repairs or replacements, and the 
maximisation of asset lifespans. This structured approach 
ensures that maintenance priorities are met efficiently 
and cost-effectively.
 5. Performance Metrics and Continuous 
Improvement
 Defining and measuring key performance indicators 
(KPIs) will provide valuable insights into the effectiveness 
of maintenance activities. Regular reviews, informed by 
client and staff feedback, will drive a culture of continuous 
improvement and operational excellence.
 Proven Expertise
 By implementing these solutions, PortmanDentex can 
expect to achieve several significant benefits:
 Reduced Disruptions: Proactive maintenance and real
t
 ime tracking will minimise unexpected breakdowns, 
ensuring seamless operations.
 Improved Efficiency: Streamlined processes and 
advanced technologies will optimise resource 
management and operational workflows.
 Maximised Asset Lifespan: Effective asset 
management ensures equipment and facilities 
remain in peak condition, extending their operational 
lifespan.
 Continuous Improvement: Data-driven insights 
and regular process reviews will foster ongoing 
enhancements in service delivery and operational 
performance.
 By leveraging these best practices, PortmanDentex will 
enhance maintenance delivery across its estate, improving 
service quality and operational performance while 
ensuring long-term sustainability.
 R&M SPEND AS % OF TURNOVER 
Q: In your experience, for a company such as 
PortmanDentex, what is considered to be best 
in class in terms of ongoing operating costs 
as a percentage of revenue for Repairs and 
Maintenance?
 A: In industries such as dental practices and healthcare 
services, determining what constitutes “best-in-class” 
Repairs and Maintenance (R&M) costs as a percentage of 
revenue depends on several factors, including the scale of 
operations, the age and condition of the facilities, and the 
level of equipment used.
 For a company like PortmanDentex, which operates in the 
dental sector and emphasises high-quality facilities and 
equipment, a good benchmark would typically fall within 
the range of 2% to 5% of revenue for R&M.
 Q18 
INNOVATION
 Q: Describe the innovation you propose to bring 
to PortmanDentex to drive improvements in 
efficiency and effectiveness. Your answer should 
include technology, tools, ways of working and 
processes you intend to deploy. Please illustrate 
providing examples of where you have delivered 
innovation to your existing clients. 
A: To meet these needs, we propose a comprehensive 
innovation strategy that integrates cutting-edge 
technology, robust tools, and efficient processes.
 Deployment of the Facilio CAFM System
 At the core of this strategy is the implementation of the 
Facilio CAFM system, a powerful platform designed to:
 Manage tasks and track progress seamlessly.
 Provide real-time updates and activity tracking.
 Facilitate clear and efficient communication.
 This system will empower PortmanDentex with 
transparent and efficient operations, ensuring better 
decision-making and streamlined workflows.
 Predictive Analytics and Preventive  
Maintenance Protocols
 We will implement predictive analytics alongside 
preventive maintenance strategies to identify and resolve 
potential issues before they disrupt operations. This 
proactive approach will:
 15
Q19 
Ensure smoother day-to-day operations.
 Deliver cost savings.
 Extend the lifespan of critical assets.
 Energy Reduction and Renewable Expertise
 Through our collaboration with Carbon Dot, a specialist 
in energy reduction and renewable strategies, we can 
provide tailored solutions to drive energy efficiency. 
Whether supporting PortmanDentex’s net-zero 
commitments or managing ad hoc asset replacements for 
improved efficiency, this partnership ensures sustainable 
energy management aligned with operational goals.
 Proven Expertise
 Our commitment to innovation and efficiency is evidenced 
by our successful partnerships:
 Facilio CAFM Implementation: Proven to significantly 
improve task management and communication for 
clients, resulting in enhanced operational efficiency 
and transparency.
 Predictive Analytics and Preventive Maintenance: 
Successfully deployed strategies have reduced 
downtime, improved asset longevity, and delivered 
measurable cost savings.
 Outcomes
 By adopting these solutions, PortmanDentex can expect 
numerous benefits, including:
 Enhanced Operational Efficiency: Achieved 
through real-time task management, seamless 
communication, and streamlined workflows.
 Improved Asset Longevity: Predictive analytics and 
preventive maintenance will reduce disruptions and 
prolong asset lifespans.
 Energy Savings: Tailored energy strategies and 
renewable solutions delivered through Carbon Dot 
will contribute to cost reductions and sustainability 
goals.
 Transparency and Informed Decision-Making: Regular 
updates, detailed reports, and advanced analytics will 
foster trust and drive better decisions.
 Culture of Continuous Improvement: A collaborative 
environment where innovative ideas are encouraged, 
evaluated, and implemented.
 MOBILISATION 
Q: Describe your approach to mobilisation and 
transition of the services. In your answer include 
a project plan, your mobilisation methodology, 
risks & timescales.
 A: We understand that a smooth and seamless transition 
is essential to avoid disruption and to ensure continuity 
of services. Our mobilisation approach is thorough, 
collaborative, and designed to make the process as 
straightforward and efficient as possible for you and your 
teams.
 We pride ourselves on being personable, flexible, 
and approachable. While we bring a tried-and-tested 
methodology to the table, we adapt our approach to 
suit the unique needs of your practices. Here’s how we 
envision working with you:
 Dedicated Mobilisation Team
 We assign a dedicated mobilisation team, including your 
Account manager, a Project Manager, Helpdesk Lead, and 
Compliance Specialist. This team will oversee every aspect 
of mobilisation, ensuring all key milestones are achieved 
within the agreed timeframe.
 Collaboration is Key
 We value open and transparent communication. We’ll 
work closely with your team, relying on your insights to 
provide essential information such as PPM schedules, 
relevant documentation, and details about any current 
partners you’d like to continue working with (such as 
possibly your specialist contractors). Together, we’ll create 
a solid foundation for success.
 Project Plan
 We kick things off with a robust project plan tailored to 
your needs. This will outline:
 Clear timelines.
 Key milestones.
 Resource allocation.
 Deliverables for both parties.
 Regular progress reviews will keep everyone aligned 
and ensure we meet our objectives.
 Site Visits and Familiarisation
 Our team (including your dedicated Helpdesk) will usually 
visit your sites to meet Practice Managers, understand 
operations, and identify any unique requirements. This 
ensures we’re prepared to hit the ground running on day 
one and gives everybody a good understanding of what is 
16
 important to you. 
17
 Client Manual Creation
 We’ll create a bespoke “Client Manual” during 
mobilisation. This living document will be our go-to 
reference for operational procedures, contacts, and 
service details. It evolves alongside your needs, ensuring it 
always reflects the most up-to-date information.
 Portal Training and Onboarding
 Training is a top priority. We’ll make sure your team is 
comfortable using the Facilio portal, scheduling sessions 
at times that suit your Practice Managers and key 
stakeholders. We keep the training engaging and practical, 
ensuring everyone feels confident logging tasks and 
accessing reports. We then follow this up with a portal 
training video, to reference back to. 
Set Go-Live or Staggered Transition
 While we recommend a set go-live date to provide clarity 
and consistency, we’re happy to stagger the transition 
across sites if that works better for you. Either way, we’ll 
ensure everyone feels supported throughout.
 Post-Go-Live Support
 We don’t just leave you to figure things out. For the first 
few months post-go-live, our mobilisation team will be 
on hand to provide extra support, answer questions, and 
ensure any teething issues are resolved quickly.

 PHASE ACTIVITY STAKEHOLDER MANAGEMENT DELIVERABLES TIMEFRAME
 Initiation Establish mobilisation team and 
assign roles.
 Introduce key contacts to PortmanDentex 
stakeholders; outline mobilisation 
strategy and communication plan.
 Mobilisation 
structure, roles, and 
communication plan.
 Week 1
 Kick-off Meeting Formal project launch to align 
on objectives, SLAs, KPIs, and 
timelines.
 Host meeting with PortmanDentex teams 
to share goals, address concerns, and 
align on milestones.
 Kick-off presentation, 
documented SLAs/KPIs.
 Week 2
 Data Collection Gather asset registers, PPM 
schedules, compliance 
documents, and operational 
insights.
 Weekly meeting to review progress. Comprehensive data set 
covering reactive and 
compliance.
 Weeks 2-4
 Site 
Familiarisation
 Conduct site audits and 
condition surveys. Engage 
with Practice Managers for 
operational insights.
 Share findings with PortmanDentex 
teams, highlighting key observations  
and gaps.
 Site audit reports, risk 
register.
 Weeks 3-5
 Transition 
Planning
 Develop a bespoke Client 
Manual and service transition 
plan.
 Ensure PortmanDentex teams have 
access to the Client Manual drafts for 
review and input.
 Client Manual, transition 
plan.
 Weeks 4-6
 Compliance 
Review
 Verify compliance with 
statutory and industry 
standards (e.g., SFG20).
 Regular updates to PortmanDentex 
compliance teams on progress and 
identified gaps.
 Compliance checklist, 
gap analysis.
 Weeks 4-6
 System 
Integration
 Configure CAFM system 
and integrate with existing 
PortmanDentex systems, if 
applicable.
 Schedule training sessions for 
PortmanDentex teams on the system’s 
functionalities.
 CAFM system 
configuration, user 
training materials.
 Weeks 5-7
 Training Conduct training sessions for 
FM staff and PortmanDentex 
stakeholders on processes and 
systems.
 Provide training schedules and feedback 
opportunities for Practice Managers and 
teams.
 Training completion logs, 
feedback forms.
 Weeks 6-8
 Go-Live 
Preparation
 Final checks and phased testing 
of systems and processes.
 Share readiness updates and Go
Live checklist with PortmanDentex 
stakeholders.
 Go-Live readiness 
report.
 Weeks 7-9
 Go-Live Transition to full-service 
delivery, ensuring Help Desk 
and support systems are 
operational.
 Maintain open communication channels 
for real-time support; provide a 
dedicated escalation contact.
 Seamless service 
transition.
 Week 10
 Post-Go-Live 
Support
 Conduct a 100-day review 
to assess performance and 
address any gaps.
 Host review sessions with PortmanDentex 
to evaluate service delivery and collect 
feedback.
 Post-Go-Live review 
report, improvement 
plan.
 Weeks 11-14
18
 RISK DESCRIPTION MITIGATION STRATEGY
 Incomplete Information Missing or inaccurate data such as PPM 
schedules, asset details, or existing 
contractor agreements.
  Collaborate with the client’s team early to gather essential 
documents and data.
  Perform a gap analysis to identify missing information.
 Operational Disruption Interruptions to daily operations during 
mobilisation and transition.
  Conduct detailed site visits to identify potential challenges and 
operational needs upfront.
  Develop a phased or flexible Go-Live plan to minimise disruption.
  Maintain regular communication with site teams and key 
stakeholders.
 Compliance Gaps Non-compliance with statutory or 
regulatory requirements pre-transition.
  Perform a comprehensive pre-mobilisation compliance audit.
  Work with the client’s team to address and prioritise compliance 
gaps.
  Create an ongoing compliance monitoring schedule.
 Stakeholder Misalignment Lack of engagement or buy-in from client 
stakeholders or site teams.
  Schedule stakeholder briefings and workshops to align 
expectations and goals.
  Develop a stakeholder engagement plan tailored to various roles.
  Appoint site-level champions to ensure local-level support and 
communication.
 Training Deficiencies Insufficient or inconsistent training for staff 
on new systems, processes, or expectations.
  Provide comprehensive and flexible training programs (online, 
in-person, or hybrid).
  Include refresher training and knowledge-sharing sessions post
Go-Live.
  Collect and act on feedback to continuously improve training 
effectiveness.
 Communication Breakdown Miscommunication between teams, 
stakeholders, or contractors during 
mobilisation.
  Establish a centralised communication platform for updates and 
collaboration.
  Share regular progress updates and key milestones with all 
stakeholders.
  Assign a communication lead to manage and oversee messaging.
 Cultural Resistance Resistance from staff to new processes, 
policies, or service providers.
  Engage teams early by explaining the benefits of the new 
processes and services.
  Provide ongoing support and open forums to address concerns.
  Use change management techniques to ease transitions.
 Site-Specific Challenges Unique or unforeseen challenges at 
individual sites.
  Conduct site-specific surveys and assessments early in the 
mobilisation process.
  Customise mobilisation plans to address individual site needs.
  Monitor progress and escalate issues promptly for resolution.
 We’re excited about the opportunity to work with PortmanDentex and bring our expertise to your practices. By working 
together, we’ll ensure a mobilisation process that’s as effortless and effective as possible, leaving you free to focus on 
what matters most: delivering excellent patient care.
DUE DILIGENCE
 Q: Please describe your approach to due diligence. 
E.g. asset verification and condition surveys. In 
your answer please include typical methodology 
t
 iming and duration of due diligence.
 A: At IEM, we ensure a robust due diligence process by 
leveraging technology, supply chain verification, and 
rigorous quality control. Below is a detailed outline of our 
approach:
 1. Supply Chain Competence Verification
 We utilise SafeContractor to verify the competence of all 
supply chain partners. This ensures that each contractor 
meets our required standards for health, safety, and 
operational performance.
 2. Automated Checks via Facilio System
 Our CAFM system, Facilio, plays a critical role in due 
diligence by automating key checks:
 Work Order Verification: When a work order is 
booked, Facilio performs automated checks to ensure 
the task is appropriate and assigned to a qualified 
engineer.
 Geolocation Tracking: Facilio ensures that engineers 
are on-site by verifying geolocation data during PPM 
(Planned Preventative Maintenance) tasks.
 Certification Control: Tasks cannot be closed without 
the appropriate certification being uploaded. Facilio 
enforces this by blocking task closure until all required 
documentation is attached.
 3. Document Verification
 Once documentation is uploaded, it undergoes a 
thorough verification process:
 Job Sheet Review: All reactive and completed works 
are checked to confirm completion, identify follow-on 
tasks, and ensure cost accuracy.
 Compliance Certification Checks: Our compliance 
team reviews certifications to ensure they meet 
industry best practices and regulatory requirements.
 4. Remedial Works Management
 All identified remedial works are captured in the system 
and sent to the client for review. Partners are responsible 
for progressing these works to costing within the agreed 
SLAs (Service Level Agreements).
 Field operatives conduct audits of a percentage of tasks 
on-site to ensure supply chain quality. These audits are 
recorded using the Facilio system, allowing for real-time 
review and feedback.
 6. Continuous Improvement
 Feedback from audits and compliance checks is used 
to continuously improve our processes, ensuring that 
we maintain high-quality standards and meet client 
expectations.
 This comprehensive due diligence approach ensures that 
all tasks are completed to the highest standard, with full 
transparency and accountability at every stage of the 
process.
 Q21 
ASSET REGISTER
 Q: Confirm your approach to creating a complete 
Asset Register should be you successful in 
this RFP. Explain how information would be 
captured, over what timeline and whether there 
are any additional costs involved in doing so. 
A: We provide a robust and comprehensive approach 
to asset management through our advanced CAFM 
system. Our asset management module is designed to 
capture and maintain critical information on asset history, 
condition, maintenance, cost tracking, and lifecycle 
management.
 Using standardised asset capture templates, our 
supply chain systematically records all necessary asset 
information and supporting documentation. Each asset 
is mapped to the relevant compliance activity, ensuring 
a clear record of maintenance and compliance actions 
carried out in accordance with SFG20 standards. This 
process guarantees transparency and demonstrates 
adherence to established compliance requirements.
 Through detailed condition ratings, we develop lifecycle 
plans and forecasts that enable our clients to make 
informed decisions regarding asset replacement 
strategies. Additionally, by uploading final data for each 
asset, we provide insights into asset depreciation, helping 
clients manage their portfolios with greater financial 
foresight.
 With IEM’s comprehensive asset management solutions, 
our clients can rely on a seamless, data-driven approach 
to maintaining their facilities efficiently and in compliance 
with industry standards.
 19
Q22 
and continuous improvement, ensuring excellence across 
all projects.
 SUPPLY CHAIN
 Q: 1) Describe your supplier selection process 
for your supply chain– Describe how you ensure fair and transparent 
treatment of your supply chain– Describe how you manage performance within 
your supply chain– Describe how you deal with disputes within your 
supply chain
 A: Supplier Selection Process 
IEM employs a meticulous supplier selection process to 
ensure collaboration with high-quality contractors and 
sub-contractors. We begin with a thorough assessment 
of potential suppliers, evaluating capabilities, financial 
stability, and track record. This is followed by rigorous 
onboarding, including verification of credentials, 
compliance with industry standards, and commitment to 
continuous improvement.
 Our extensive network of over 1500 contractors spans all 
hard FM disciplines. This network is regularly monitored 
by our supply chain manager, ensuring adherence to high 
standards and reliable service delivery.
 Outcomes:
 Our process ensures seamless, high-quality services for 
clients by engaging only compliant and capable suppliers. 
This minimises risks and ensures timely, cost-effective 
project delivery.
 Ensuring Fair and Transparent Treatment
 We prioritise fairness and transparency in managing our 
supply chain to maintain trust and efficiency. We establish 
clear terms and SLAs, conduct thorough onboarding 
with probation periods, and perform regular reviews of 
contractor performance. Feedback mechanisms and Safe 
Contractor accreditation reinforce our commitment to 
ethical and safe practices, complemented by National 
Living Wage accreditation.
 Outcomes:
 This approach fosters collaboration, enhances service 
delivery, and ensures equitable treatment of all supply 
chain partners.
 Performance Management
 We oversee performance through KPIs, regular audits, 
feedback, and ongoing contractor training. Evidence of 
our success includes managing 400–450 weekly reactive 
tasks for a year without claims, supported by robust 
reporting and communication.
 Outcomes:
 Clients benefit from consistent quality, reliable services, 
Dispute Resolution
 Disputes are resolved via clear communication, 
contractual clarity, mediation, and escalation protocols. 
Lessons learned are integrated into processes for 
continuous improvement.
 Outcomes:
 Prompt dispute resolution minimises disruptions, 
preserves relationships, and ensures project success.
 Q23 
CLEANING AND WINDOW CLEANING
 Q: Describe your capability with regard to 
contract cleaning services and window cleaning. 
Please note, that contract cleaning and window cleaning is 
out of scope of this RFP but PortmanDentex would like to 
obtain a brief description of your capability at this stage for 
future opportunities. 
A: At IEM, we do not currently offer window cleaning 
services directly; however, this is an area we could readily 
incorporate into our offerings if it became a requirement 
for PortmanDentex in the future. We have access to 
reliable partners with expertise in window cleaning, 
ensuring any services provided would align with our high 
standards of quality and professionalism.
 Q24 
CDM
 Q: Describe your approach to ensuring CDM 
compliance regulations including but not 
limited to RAMS, contractor selection, training 
and the share and transfer of information 
(e.g. asbestos surveys and instruction of R&D 
surveys). Include in your response how you will 
aid us to meet and fulfil our client duties under 
these regulations and your processes regarding 
notifiable works. 
Provision of Information to Duty Holders:– How do you ensure relevant pre-construction 
information is provided to designers and 
contractors? (such as asbestos surveys, site 
plans)– What pre-construction information do you 
provide routinely / what would you source on 
demand?
 20
safety-critical information is shared effectively. IEM ensure – What is your approach to arranging R&D surveys 
where required? How are you proactive in this 
approach when booking in works?– How do you ensure welfare facilities are provided 
on-site? Is this asked and checked when booking 
works?
 Ensuring Competence:– How do you vet contractors to ensure they are 
competent under CDM? (ensuring they have the 
skills, knowledge, and experience to perform 
their roles safely and competently)– What checks are performed beyond verifying 
insurance and SSIP schemes?– How are these checks documented?
 Quality Assurance and Oversight:– How do you ensure risks are identified and 
managed throughout the project? (CPP, RAMS 
etc) Where are these held?– Do you review the CPPs, RAMS for adequacy?– Do you carry out physical inspections of work 
conducted by contractors (at the time they 
works are being completed)? What proportion of 
contractor works are physically checked?– How can we gain visibility of these inspections 
and contractor ratings?
 A: Under CDM regulations 2015, IEM’s approach 
ensures the health, safety, and welfare of all personnel 
working on site. We ensure all responsibilities are clearly 
understood and that duties under the regulations are 
met, particularly regarding risk assessment, contractor 
selection, training, and the sharing of key safety 
information. RAMS are comprehensive for all work 
activities, ensuring that identified risks are evaluated 
and mitigated. They are created in consultation with the 
project team, contractors, and other stakeholders. They’re 
reviewed and updated regularly to reflect changes on 
site or in scope. Our RAMS process ensures that risks are 
proactively managed, and safe working practices are in 
place prior to commencement of work. Our contractor 
selection process includes a thorough vetting procedure, 
ensuring that all contractors are competent, qualified, 
and able to demonstrate their commitment to health 
and safety. We assess their previous project experience, 
review their health and safety policies, and check their 
insurance, certifications, and safety track record. Only 
contractors who meet our strict CDM compliance criteria 
are appointed. Personnel are continuously upskilled 
and updated with relevant training, ensuring they are 
competent to perform their roles safely. This may include 
site-specific inductions, health and safety training (e.g., 
asbestos awareness, working at height), and ongoing 
toolbox talks. Clear communication is key to ensuring that 
that all relevant surveys and risk assessments are shared 
with contractors at the planning stage, and that these 
documents are regularly reviewed. Information is stored 
in a central database and made readily available to all 
personnel, ensuring easy access and transparency.IEM will 
work closely with the client to ensure that the Principal 
Designer and Principal Contractor roles are supported and 
that all safety and compliance measures are met. We will 
assist in developing and reviewing the Health and Safety 
File, ensuring that it contains all necessary documents and 
that the project complies with notification requirements 
to the Health and Safety Executive (HSE). For notifiable 
works (Duration of the project exceeds 30 days for 20 
people or more than 500 person days),IEM will ensure 
the HSE is notified in accordance with guidelines. This 
includes providing all necessary documentation prior to 
the start of work, including risk assessments, method 
statements, and details of the contractors. We’ll provide 
regular updates on the progress of notifiable works, 
ensuring that any changes or risks are communicated and 
managed promptly. Our team is dedicated to ensuring 
full compliance with CDM regulations through detailed 
planning, thorough risk assessments, careful selection 
of contractors, ongoing training, and communication. 
By collaborating closely with you, we will ensure the 
successful and safe delivery of the project, meeting all 
regulatory requirements and ensuring the well-being of 
everyone involved.
 Q25 
APPROVALS OF EXPENDITURE
 Q: How does your system automate spend 
approval that is required centrally by 
PortmanDentex?
 What best practice can you share with PortmanDentex 
to ensure strong cost control balanced with being able to 
complete work on site when in attendance without delay? 
Within your response, provide examples of how this works 
with your other clients of a comparable business operation 
and what your recommendation would be in terms of value 
of Work Orders that can be completed without further central 
approval. Would this recommendation change depending on 
the Priority level (i.e. higher threshold for a P1 and so on)?
 A: At IEM we have a robust system that automates spend 
approvals within our Facilio system, tailored to meet the 
specific needs of our clients.
 Facilio is designed to streamline the approval process 
by setting predefined thresholds for different types of 
work orders. These thresholds can be adjusted based on 
different criteria such as different areas/regions, price and 
the type of work order – This can be easily changed if your 
21
approval structure needed to be amended in the future 
Q26 
and we can have several different approval levels if this 
is required, all managed within the system providing full 
visibility to stakeholders.
 For example, with our client IVC Vets, which operates 
across 1400 sites, we have implemented a tiered approval 
process. IVC requested a structure so that all quotes 
are reviewed by their FM team in the first instance, if 
the quotation is under £5000 this does not require a 
further approval, if it is above £5000 once the FM team 
have approved this, this would then go to the secondary 
approver, in this case the Area Manager; ensuring that all 
expenditures are monitored and controlled effectively.
 With regards to reactive tasks, many of our clients have 
agreed a £750 budget, allowing our Supply Chain Partners 
to proceed without delay. With urgent tasks where these 
may go over the budget, our Supply Chain Partners are 
able to request an uplift onsite to avoid delay, in this 
instance we could contact Portmen Dentex for approval, 
or have a higher internal approval limit for specific tasks 
that are more urgent, this ensures that urgent issues are 
addressed promptly, while still maintaining oversight on 
spending; we are very flexible and able to work to your 
needs on this.
 By implementing these automated spend approvals, 
PortmanDentex can expect several benefits:
 1. **Enhanced Operational Efficiency**
 Immediate response to high-priority issues without 
waiting for manual approvals, reducing downtime and 
potential disruptions.
 2. **Cost Control**
 Centralised monitoring of expenditures, ensuring that all 
spending is within budget and justified.
 3. **Transparency**
 Clear documentation and tracking of all spend approvals, 
providing an audit trail that supports accountability and 
f
 inancial oversight.
 4. **Flexibility**
 The ability to adjust approval thresholds based on the 
priority of the task, ensuring that urgent repairs are 
prioritised while maintaining control over less critical 
expenditures.
 We are confident that this approach will provide 
PortmanDentex with the control and flexibility needed to 
maintain operational excellence.
 ACCREDITATIONS AND CERTIFICATIONS
 Q: What accreditations / certifications / SSIP  
do you hold?
 Please provide supporting evidence of such accreditations.
 A: We recognise the importance of maintaining high 
standards in our operations and ensuring the safety and 
quality of our services. IEM proudly holds the following 
accreditations and certifications:
 ISO9001
 Demonstrating our commitment to quality management 
systems, ensuring that we consistently meet customer 
and regulatory requirements.
 ISO14001
 Highlighting our dedication to environmental 
management, reflecting our efforts to minimise our 
environmental impact and promote sustainability.
 ISO45001
 This certification underscores our commitment to health 
and safety management, ensuring a safe and healthy 
workplace for our employees and stakeholders.
 Safe Contractor SSIP
 This accreditation verifies our compliance with health 
and safety regulations, showcasing our dedication to 
maintaining a safe working environment.
 Principal Safety
 This certification further emphasises our commitment 
to safety, ensuring that we adhere to stringent safety 
standards in all our operations.
 National Living Wage Accredited
 Reflecting our commitment to fair pay practices that 
support employee well-being, enhance job satisfaction, 
and foster a motivated workforce, ultimately driving 
excellence in the services we provide.
 In addition to these certifications, we are also members 
of several esteemed trade associations, which further 
validate our commitment to industry standards and 
continuous improvement
 IWFM
 Our membership with the Institute of Workplace and 
Facilities Management demonstrates our dedication to 
excellence in facilities management.
 IET
 Being a member of the Institution of Engineering and 
Technology highlights our commitment to engineering 
excellence and innovation.
 22
These accreditations and memberships are not just 
badges of honour; they are integral to our operational 
ethos. They ensure that we consistently deliver high
quality services while prioritising safety, environmental 
sustainability, and continuous improvement.
 By holding these accreditations and memberships, we 
assure our clients of our unwavering commitment to 
quality, safety, and environmental responsibility. These 
certifications provide confidence that our operations are 
conducted to the highest standards, resulting in reliable 
and superior service delivery. Our clients can trust that 
we will meet their needs efficiently and effectively, always 
adhering to best practices and regulatory requirements.
 Please refer to copies of accreditations and certificates in 
the appendix, sections 2.1 through 2.4w
 What do the next 12 months look like for us?
 Along with keeping all our current accreditations, we are 
now starting our journey to becoming one of the very few 
FM providers who are B Corp accredited.
 Q27 
WHY YOU?
 Q: Why should PortmanDentex consider 
you to be their FM partner? Please outline 
why you believe you are best placed to meet 
PortmanDentex’s objectives? Please let us know 
any other information you think is pertinent at 
this stage.
 A: IEM is eager to embark on a collaborative journey 
with Portman Dentex, which is centred around our 
substantial experience is delivering across comparable 
multi-site estates all in a similar condition, we have first 
hand understand of what to watch for and where to 
focus support and delivery through current experience, 
this added to the ability to mobilise across the entire 
estate with ease, all due to the current contract we have 
with similar clients covering 1,200+ buildings of a similar 
nature.
 Our absolute commitment to transparency, accountability, 
and innovation ensures that our partnership will be 
characterised by open communication, mutual trust, and 
a shared commitment to excellence, whilst we support 
your journey.
 By leveraging advanced technology like our “Facilio” 
CAFM system and drawing upon our extensive experience 
in managing complex frameworks and requirements, 
including our successful collaborations with organisations 
like NHS & IVC, we are very well-equipped to support 
Portman Dentex in achieving your goals.
 If you are after a cost effective, dedicated delivery team 
who are experts in Building compliance across multi-site 
estates, with the added bonus of being already set up to 
support you with our operational partner network then 
IEM Facilities Management is what you need.




    """
    question = user_input
    # Combine context and question
    input_text = f"Context: {context}\n\nQuestion: {question}\nAnswer:"
    
   
    response = co.generate(
        model="c4ai-aya-expanse-32b",
        prompt=input_text,
        max_tokens=10000
    )
    
    # Print the response
    #print("Answer:", response.generations[0].text)
    
    st.success(response.generations[0].text)
