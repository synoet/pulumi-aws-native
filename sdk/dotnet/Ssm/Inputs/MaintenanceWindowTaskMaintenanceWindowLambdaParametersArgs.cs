// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ssm.Inputs
{

    public sealed class MaintenanceWindowTaskMaintenanceWindowLambdaParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("clientContext")]
        public Input<string>? ClientContext { get; set; }

        [Input("payload")]
        public Input<string>? Payload { get; set; }

        [Input("qualifier")]
        public Input<string>? Qualifier { get; set; }

        public MaintenanceWindowTaskMaintenanceWindowLambdaParametersArgs()
        {
        }
        public static new MaintenanceWindowTaskMaintenanceWindowLambdaParametersArgs Empty => new MaintenanceWindowTaskMaintenanceWindowLambdaParametersArgs();
    }
}
