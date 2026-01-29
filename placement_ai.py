def placement_path(college, branch, skills, lang):
    if lang == "hindi":
        return f"""
🎓 डेमो करियर रोडमैप

कॉलेज: {college}
ब्रांच: {branch}
स्किल्स: {skills}

अगले 3 महीने:
1️⃣ DSA और बेसिक्स मजबूत करें  
2️⃣ 2 छोटे प्रोजेक्ट बनाएं  
3️⃣ Python/C पर अभ्यास करें  
4️⃣ मॉक इंटरव्यू दें  

फ्री संसाधन:
• YouTube
• GeeksForGeeks
• LeetCode
"""
    else:
        return f"""
🎓 Demo Career Roadmap

College: {college}
Branch: {branch}
Skills: {skills}

Next 3 months:
1️⃣ Strengthen DSA fundamentals  
2️⃣ Build 2 mini projects  
3️⃣ Practice Python/C daily  
4️⃣ Give mock interviews  

Free resources:
• YouTube
• GeeksForGeeks
• LeetCode
"""
