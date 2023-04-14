// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2.Outputs
{

    [OutputType]
    public sealed class ApiGatewayManagedOverridesStageOverrides
    {
        public readonly Outputs.ApiGatewayManagedOverridesAccessLogSettings? AccessLogSettings;
        public readonly bool? AutoDeploy;
        public readonly Outputs.ApiGatewayManagedOverridesRouteSettings? DefaultRouteSettings;
        public readonly string? Description;
        public readonly object? RouteSettings;
        public readonly object? StageVariables;

        [OutputConstructor]
        private ApiGatewayManagedOverridesStageOverrides(
            Outputs.ApiGatewayManagedOverridesAccessLogSettings? accessLogSettings,

            bool? autoDeploy,

            Outputs.ApiGatewayManagedOverridesRouteSettings? defaultRouteSettings,

            string? description,

            object? routeSettings,

            object? stageVariables)
        {
            AccessLogSettings = accessLogSettings;
            AutoDeploy = autoDeploy;
            DefaultRouteSettings = defaultRouteSettings;
            Description = description;
            RouteSettings = routeSettings;
            StageVariables = stageVariables;
        }
    }
}
