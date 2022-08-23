// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Outputs
{

    /// <summary>
    /// &lt;p&gt;A configuration for a streaming session.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class LaunchProfileStreamConfiguration
    {
        public readonly Pulumi.AwsNative.NimbleStudio.LaunchProfileStreamingClipboardMode ClipboardMode;
        /// <summary>
        /// &lt;p&gt;The EC2 instance types that users can select from when launching a streaming session
        ///             with this launch profile.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.NimbleStudio.LaunchProfileStreamingInstanceType> Ec2InstanceTypes;
        /// <summary>
        /// &lt;p&gt;The length of time, in minutes, that a streaming session can be active before it is
        ///             stopped or terminated. After this point, Nimble Studio automatically terminates or
        ///             stops the session. The default length of time is 690 minutes, and the maximum length of
        ///             time is 30 days.&lt;/p&gt;
        /// </summary>
        public readonly double? MaxSessionLengthInMinutes;
        /// <summary>
        /// &lt;p&gt;Integer that determines if you can start and stop your sessions and how long a session
        ///             can stay in the STOPPED state. The default value is 0. The maximum value is 5760.&lt;/p&gt;
        ///         &lt;p&gt;If the value is missing or set to 0, your sessions can’t be stopped. If you then call
        ///                 &lt;code&gt;StopStreamingSession&lt;/code&gt;, the session fails. If the time that a session
        ///             stays in the READY state exceeds the &lt;code&gt;maxSessionLengthInMinutes&lt;/code&gt; value, the
        ///             session will automatically be terminated (instead of stopped).&lt;/p&gt;
        ///         &lt;p&gt;If the value is set to a positive number, the session can be stopped. You can call
        ///                 &lt;code&gt;StopStreamingSession&lt;/code&gt; to stop sessions in the READY state. If the time
        ///             that a session stays in the READY state exceeds the
        ///                 &lt;code&gt;maxSessionLengthInMinutes&lt;/code&gt; value, the session will automatically be
        ///             stopped (instead of terminated).&lt;/p&gt;
        /// </summary>
        public readonly double? MaxStoppedSessionLengthInMinutes;
        public readonly Outputs.LaunchProfileStreamConfigurationSessionStorage? SessionStorage;
        /// <summary>
        /// &lt;p&gt;The streaming images that users can select from when launching a streaming session
        ///             with this launch profile.&lt;/p&gt;
        /// </summary>
        public readonly ImmutableArray<string> StreamingImageIds;

        [OutputConstructor]
        private LaunchProfileStreamConfiguration(
            Pulumi.AwsNative.NimbleStudio.LaunchProfileStreamingClipboardMode clipboardMode,

            ImmutableArray<Pulumi.AwsNative.NimbleStudio.LaunchProfileStreamingInstanceType> ec2InstanceTypes,

            double? maxSessionLengthInMinutes,

            double? maxStoppedSessionLengthInMinutes,

            Outputs.LaunchProfileStreamConfigurationSessionStorage? sessionStorage,

            ImmutableArray<string> streamingImageIds)
        {
            ClipboardMode = clipboardMode;
            Ec2InstanceTypes = ec2InstanceTypes;
            MaxSessionLengthInMinutes = maxSessionLengthInMinutes;
            MaxStoppedSessionLengthInMinutes = maxStoppedSessionLengthInMinutes;
            SessionStorage = sessionStorage;
            StreamingImageIds = streamingImageIds;
        }
    }
}
