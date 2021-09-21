// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync.Inputs
{

    public sealed class DataSourceRelationalDatabaseConfigArgs : Pulumi.ResourceArgs
    {
        [Input("rdsHttpEndpointConfig")]
        public Input<Inputs.DataSourceRdsHttpEndpointConfigArgs>? RdsHttpEndpointConfig { get; set; }

        [Input("relationalDatabaseSourceType", required: true)]
        public Input<string> RelationalDatabaseSourceType { get; set; } = null!;

        public DataSourceRelationalDatabaseConfigArgs()
        {
        }
    }
}
