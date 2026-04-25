import React from 'react';
import { ArrowLeft } from 'lucide-react';

const Section = ({ number, title, children }) => (
    <div>
        <h2 className="text-lg font-bold text-gray-900 mb-3">
            <span className="text-emerald-600">{number}.</span> {title}
        </h2>
        <div className="text-gray-600 leading-relaxed">{children}</div>
    </div>
);

const PrivacyPolicyView = ({ onBack }) => {
    return (
        <div className="min-h-screen bg-gray-50">
            <div className="bg-white border-b border-gray-200 sticky top-0 z-10">
                <div className="max-w-3xl mx-auto px-4 py-4">
                    <button
                        onClick={onBack}
                        className="flex items-center space-x-2 text-emerald-600 hover:text-emerald-700 transition font-medium"
                    >
                        <ArrowLeft className="w-5 h-5" />
                        <span>Back</span>
                    </button>
                </div>
            </div>

            <div className="max-w-3xl mx-auto px-4 py-10">
                <h1 className="text-3xl font-bold text-gray-900 mb-2">PolyBot Privacy Policy</h1>
                <p className="text-sm text-gray-500 mb-10">Last updated: April 2026</p>

                <div className="space-y-8">
                    <Section number="1" title="Who we are">
                        <p>PolyBot is a free AI-powered language learning application operated by Jeff Karkari-Apau, based in Peterborough, United Kingdom. For privacy enquiries, contact: <a href="mailto:jeff.itservices@gmail.com" className="text-emerald-600 hover:underline">jeff.itservices@gmail.com</a></p>
                    </Section>

                    <Section number="2" title="What data we collect">
                        <p>When you sign in with Google, we receive your name and email address from Google. We store this alongside your learning activity: lesson progress, XP points, streaks, vocabulary scores, and spaced repetition review history.</p>
                        <p className="mt-3">We do not collect payment information, location data, or any data beyond what is necessary to provide the learning experience.</p>
                    </Section>

                    <Section number="3" title="Why we collect it">
                        <p>We process your data to provide the PolyBot service — specifically to save your progress, personalise your learning experience, and restore your session when you return. The lawful basis for this processing is legitimate interests (providing the service you have signed up to use).</p>
                    </Section>

                    <Section number="4" title="Who we share it with">
                        <p className="mb-3">Your data is processed by the following third-party services solely to deliver the PolyBot service:</p>
                        <ul className="space-y-2 mb-3">
                            {[
                                ['Google', 'authentication via Google OAuth 2.0'],
                                ['MongoDB Atlas', 'cloud database storage (servers in AWS eu-west-2)'],
                                ['Microsoft Azure', 'text-to-speech voice synthesis'],
                                ['RunPod', 'AI language model inference for practice scenarios'],
                            ].map(([name, desc]) => (
                                <li key={name} className="flex items-start space-x-2">
                                    <span className="w-2 h-2 rounded-full bg-emerald-500 mt-2 flex-shrink-0" />
                                    <span><strong>{name}</strong> — {desc}</span>
                                </li>
                            ))}
                        </ul>
                        <p>No data is sold, shared for marketing purposes, or disclosed to any other third party.</p>
                    </Section>

                    <Section number="5" title="Voice data">
                        <p>If you use voice exercises, audio is recorded in your browser and sent to our backend server for transcription using OpenAI Whisper, which runs entirely within our own infrastructure. Audio is not stored — it is transcribed and immediately discarded.</p>
                    </Section>

                    <Section number="6" title="Cookies and sessions">
                        <p>PolyBot uses a single session cookie to keep you logged in. This cookie is functional and strictly necessary to provide the service. It is not used for tracking or advertising.</p>
                    </Section>

                    <Section number="7" title="How long we keep your data">
                        <p>We keep your account and learning data for as long as your account is active. If you request deletion, we will remove your data within 30 days.</p>
                    </Section>

                    <Section number="8" title="Your rights">
                        <p className="mb-3">Under UK GDPR and EU GDPR you have the right to:</p>
                        <ul className="space-y-2 mb-3">
                            {[
                                'Access the data we hold about you',
                                'Correct inaccurate data',
                                'Request deletion of your data',
                                'Object to processing',
                            ].map((right) => (
                                <li key={right} className="flex items-start space-x-2">
                                    <span className="w-2 h-2 rounded-full bg-emerald-500 mt-2 flex-shrink-0" />
                                    <span>{right}</span>
                                </li>
                            ))}
                        </ul>
                        <p>To exercise any of these rights, email <a href="mailto:jeff.itservices@gmail.com" className="text-emerald-600 hover:underline">jeff.itservices@gmail.com</a>. We will respond within 30 days.</p>
                    </Section>

                    <Section number="9" title="Data transfers">
                        <p>Some of our third-party processors operate infrastructure outside the UK and EU. Where this occurs, transfers are protected by appropriate safeguards including Standard Contractual Clauses.</p>
                    </Section>

                    <Section number="10" title="Changes to this policy">
                        <p>We may update this policy as the service develops. The date at the top of this page will reflect the most recent update.</p>
                    </Section>

                    <Section number="11" title="Supervisory authorities">
                        <p>If you are based in the UK and have concerns about how we handle your data, you can contact the Information Commissioner's Office (ICO) at <a href="https://ico.org.uk" target="_blank" rel="noopener noreferrer" className="text-emerald-600 hover:underline">ico.org.uk</a>. If you are based in the EU, you have the right to contact your local data protection authority.</p>
                    </Section>
                </div>
            </div>
        </div>
    );
};

export default PrivacyPolicyView;
