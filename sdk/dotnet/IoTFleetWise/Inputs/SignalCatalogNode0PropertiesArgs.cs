// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Inputs
{

    public sealed class SignalCatalogNode0PropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("branch")]
        public Input<Inputs.SignalCatalogBranchArgs>? Branch { get; set; }

        public SignalCatalogNode0PropertiesArgs()
        {
        }
        public static new SignalCatalogNode0PropertiesArgs Empty => new SignalCatalogNode0PropertiesArgs();
    }
}
