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
    /// Source Code Version
    /// </summary>
    public sealed class ServiceSourceCodeVersionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Source Code Version Type
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.AppRunner.ServiceSourceCodeVersionType> Type { get; set; } = null!;

        /// <summary>
        /// Source Code Version Value
        /// </summary>
        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ServiceSourceCodeVersionArgs()
        {
        }
        public static new ServiceSourceCodeVersionArgs Empty => new ServiceSourceCodeVersionArgs();
    }
}
