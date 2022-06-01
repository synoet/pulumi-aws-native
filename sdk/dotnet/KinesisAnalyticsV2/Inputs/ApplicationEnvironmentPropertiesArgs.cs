// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Inputs
{

    /// <summary>
    /// Describes execution properties for a Flink-based Kinesis Data Analytics application.
    /// </summary>
    public sealed class ApplicationEnvironmentPropertiesArgs : Pulumi.ResourceArgs
    {
        [Input("propertyGroups")]
        private InputList<Inputs.ApplicationPropertyGroupArgs>? _propertyGroups;

        /// <summary>
        /// Describes the execution property groups.
        /// </summary>
        public InputList<Inputs.ApplicationPropertyGroupArgs> PropertyGroups
        {
            get => _propertyGroups ?? (_propertyGroups = new InputList<Inputs.ApplicationPropertyGroupArgs>());
            set => _propertyGroups = value;
        }

        public ApplicationEnvironmentPropertiesArgs()
        {
        }
    }
}
