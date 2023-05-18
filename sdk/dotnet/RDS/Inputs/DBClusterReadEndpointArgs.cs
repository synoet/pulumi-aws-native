// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS.Inputs
{

    public sealed class DBClusterReadEndpointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The reader endpoint for the DB cluster.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        public DBClusterReadEndpointArgs()
        {
        }
        public static new DBClusterReadEndpointArgs Empty => new DBClusterReadEndpointArgs();
    }
}
