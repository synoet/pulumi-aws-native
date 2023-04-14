// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisDateTimeDefaultValuesArgs : global::Pulumi.ResourceArgs
    {
        [Input("dynamicValue")]
        public Input<Inputs.AnalysisDynamicDefaultValueArgs>? DynamicValue { get; set; }

        [Input("rollingDate")]
        public Input<Inputs.AnalysisRollingDateConfigurationArgs>? RollingDate { get; set; }

        [Input("staticValues")]
        private InputList<string>? _staticValues;
        public InputList<string> StaticValues
        {
            get => _staticValues ?? (_staticValues = new InputList<string>());
            set => _staticValues = value;
        }

        public AnalysisDateTimeDefaultValuesArgs()
        {
        }
        public static new AnalysisDateTimeDefaultValuesArgs Empty => new AnalysisDateTimeDefaultValuesArgs();
    }
}
