// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// Configures the inspection of login responses
    /// </summary>
    [OutputType]
    public sealed class WebAclResponseInspection
    {
        public readonly Outputs.WebAclResponseInspectionBodyContains? BodyContains;
        public readonly Outputs.WebAclResponseInspectionHeader? Header;
        public readonly Outputs.WebAclResponseInspectionJson? Json;
        public readonly Outputs.WebAclResponseInspectionStatusCode? StatusCode;

        [OutputConstructor]
        private WebAclResponseInspection(
            Outputs.WebAclResponseInspectionBodyContains? bodyContains,

            Outputs.WebAclResponseInspectionHeader? header,

            Outputs.WebAclResponseInspectionJson? json,

            Outputs.WebAclResponseInspectionStatusCode? statusCode)
        {
            BodyContains = bodyContains;
            Header = header;
            Json = json;
            StatusCode = statusCode;
        }
    }
}
