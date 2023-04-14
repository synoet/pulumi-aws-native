// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("dateTimeParameters")]
        private InputList<Inputs.DashboardDateTimeParameterArgs>? _dateTimeParameters;
        public InputList<Inputs.DashboardDateTimeParameterArgs> DateTimeParameters
        {
            get => _dateTimeParameters ?? (_dateTimeParameters = new InputList<Inputs.DashboardDateTimeParameterArgs>());
            set => _dateTimeParameters = value;
        }

        [Input("decimalParameters")]
        private InputList<Inputs.DashboardDecimalParameterArgs>? _decimalParameters;
        public InputList<Inputs.DashboardDecimalParameterArgs> DecimalParameters
        {
            get => _decimalParameters ?? (_decimalParameters = new InputList<Inputs.DashboardDecimalParameterArgs>());
            set => _decimalParameters = value;
        }

        [Input("integerParameters")]
        private InputList<Inputs.DashboardIntegerParameterArgs>? _integerParameters;
        public InputList<Inputs.DashboardIntegerParameterArgs> IntegerParameters
        {
            get => _integerParameters ?? (_integerParameters = new InputList<Inputs.DashboardIntegerParameterArgs>());
            set => _integerParameters = value;
        }

        [Input("stringParameters")]
        private InputList<Inputs.DashboardStringParameterArgs>? _stringParameters;
        public InputList<Inputs.DashboardStringParameterArgs> StringParameters
        {
            get => _stringParameters ?? (_stringParameters = new InputList<Inputs.DashboardStringParameterArgs>());
            set => _stringParameters = value;
        }

        public DashboardParametersArgs()
        {
        }
        public static new DashboardParametersArgs Empty => new DashboardParametersArgs();
    }
}
