// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner.Inputs
{

    /// <summary>
    /// Source Code configuration
    /// </summary>
    public sealed class ServiceSourceConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("authenticationConfiguration")]
        public Input<Inputs.ServiceAuthenticationConfigurationArgs>? AuthenticationConfiguration { get; set; }

        /// <summary>
        /// Auto Deployment enabled
        /// </summary>
        [Input("autoDeploymentsEnabled")]
        public Input<bool>? AutoDeploymentsEnabled { get; set; }

        [Input("codeRepository")]
        public Input<Inputs.ServiceCodeRepositoryArgs>? CodeRepository { get; set; }

        [Input("imageRepository")]
        public Input<Inputs.ServiceImageRepositoryArgs>? ImageRepository { get; set; }

        public ServiceSourceConfigurationArgs()
        {
        }
        public static new ServiceSourceConfigurationArgs Empty => new ServiceSourceConfigurationArgs();
    }
}
