// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMRServerless.Inputs
{

    public sealed class ApplicationMaximumAllowedResourcesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Per worker CPU resource. vCPU is the only supported unit and specifying vCPU is optional.
        /// </summary>
        [Input("cpu", required: true)]
        public Input<string> Cpu { get; set; } = null!;

        /// <summary>
        /// Per worker Disk resource. GB is the only supported unit and specifying GB is optional
        /// </summary>
        [Input("disk")]
        public Input<string>? Disk { get; set; }

        /// <summary>
        /// Per worker memory resource. GB is the only supported unit and specifying GB is optional.
        /// </summary>
        [Input("memory", required: true)]
        public Input<string> Memory { get; set; } = null!;

        public ApplicationMaximumAllowedResourcesArgs()
        {
        }
        public static new ApplicationMaximumAllowedResourcesArgs Empty => new ApplicationMaximumAllowedResourcesArgs();
    }
}
