// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RefactorSpaces.Inputs
{

    public sealed class RouteDefaultRouteInputArgs : Pulumi.ResourceArgs
    {
        [Input("activationState", required: true)]
        public Input<Pulumi.AwsNative.RefactorSpaces.RouteActivationState> ActivationState { get; set; } = null!;

        public RouteDefaultRouteInputArgs()
        {
        }
    }
}
